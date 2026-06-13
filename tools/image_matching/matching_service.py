"""
Image matching service for the RestArt image matching module.

This module separates the image matching service logic from the initial
prototype image utility. It compares user-captured artwork images with
candidate artwork images and returns matched image URLs with their
color cluster metadata.
"""

from typing import Any, Optional

import cv2

try:
    from .feature_matcher import align_images_orb2
    from .image_loader import load_image_from_url_with_requests
except ImportError:
    from feature_matcher import align_images_orb2
    from image_loader import load_image_from_url_with_requests


ImageUrlList = dict[str, list[Any]]
MatchedImageResult = dict[str, list[Any]]


def _load_images_from_urls(image_urls: list[str]) -> list[tuple[str, Any]]:
    """
    Load images from a list of URLs.

    Parameters
    ----------
    image_urls:
        List of image URLs.

    Returns
    -------
    list[tuple[str, Any]]
        List of image URL and loaded OpenCV image pairs.
    """
    loaded_images = []

    for url in image_urls:
        image = load_image_from_url_with_requests(str(url))

        if image is not None:
            loaded_images.append((str(url), image))

    return loaded_images


def _get_color_cluster_ratio(image_url_list: ImageUrlList, index: int) -> Optional[Any]:
    """
    Get color cluster ratio metadata by index.

    Parameters
    ----------
    image_url_list:
        Candidate artwork image data.
    index:
        Candidate image index.

    Returns
    -------
    Optional[Any]
        Color cluster ratio metadata if available.
    """
    color_cluster_ratios = image_url_list.get("color_cluster_ratio", [])

    if index < len(color_cluster_ratios):
        return color_cluster_ratios[index]

    return None


def _empty_matching_result() -> MatchedImageResult:
    """
    Create an empty matching result object.
    """
    return {
        "url": [],
        "color_cluster_ratio": [],
    }


def find_best_matching_images(
    user_images_urls: list[str],
    image_url_list: ImageUrlList,
    similarity_threshold: int = 15,
) -> MatchedImageResult:
    """
    Find the best matching artwork images for user-captured images.

    This function follows the initial prototype flow:
    1. Load candidate artwork images.
    2. Load user-captured images.
    3. Extract ORB descriptors from each user image.
    4. Compare user descriptors with each candidate image.
    5. Return matched candidate URLs and color cluster metadata.

    Parameters
    ----------
    user_images_urls:
        User-captured image URLs.
    image_url_list:
        Candidate artwork image data.
        Expected keys:
        - url
        - color_cluster_ratio
    similarity_threshold:
        Minimum feature matching score required to accept a match.

    Returns
    -------
    MatchedImageResult
        Dictionary containing matched candidate image URLs and
        corresponding color cluster ratio metadata.
    """
    candidate_urls = [str(url) for url in image_url_list.get("url", [])]

    exhibition_images = _load_images_from_urls(candidate_urls)
    user_images = _load_images_from_urls([str(url) for url in user_images_urls])

    matching_result = _empty_matching_result()

    if not exhibition_images or not user_images:
        return matching_result

    orb = cv2.ORB_create()

    for user_url, user_image in user_images:
        user_gray = cv2.cvtColor(user_image, cv2.COLOR_BGR2GRAY)
        _, user_descriptors = orb.detectAndCompute(user_gray, None)

        if user_descriptors is None:
            continue

        best_match_url = None
        best_similarity = -2
        best_candidate_index = None

        for candidate_index, (candidate_url, candidate_image) in enumerate(exhibition_images):
            similarity = align_images_orb2(user_descriptors, candidate_image)

            if similarity >= best_similarity:
                best_similarity = similarity
                best_match_url = candidate_url
                best_candidate_index = candidate_index

        if (
            best_match_url is not None
            and best_candidate_index is not None
            and best_similarity >= similarity_threshold
            and best_match_url not in matching_result["url"]
        ):
            matching_result["url"].append(best_match_url)
            matching_result["color_cluster_ratio"].append(
                _get_color_cluster_ratio(image_url_list, best_candidate_index)
            )

    return matching_result


def find_best_matching_images2(
    user_images_urls: list[str],
    image_url_list: ImageUrlList,
    similarity_threshold: int = 15,
) -> MatchedImageResult:
    """
    Compatibility wrapper for the prototype function name.

    Some prototype files used find_best_matching_images2().
    The current image matching module keeps this wrapper so that
    existing call sites can be migrated gradually.
    """
    return find_best_matching_images(
        user_images_urls=user_images_urls,
        image_url_list=image_url_list,
        similarity_threshold=similarity_threshold,
    )


def find_norm_images(
    user_images_urls: list[str],
    image_url_list: ImageUrlList,
    similarity_threshold: int = 30,
) -> MatchedImageResult:
    """
    Return normalized user image URLs with color cluster metadata.

    This function preserves the lightweight prototype behavior where
    already-selected user image URLs are passed through and paired with
    color cluster metadata by order.

    Parameters
    ----------
    user_images_urls:
        User-selected or user-captured image URLs.
    image_url_list:
        Candidate artwork image data.
        Expected keys:
        - color_cluster_ratio
    similarity_threshold:
        Kept for compatibility with the initial prototype signature.

    Returns
    -------
    MatchedImageResult
        Dictionary containing selected URLs and corresponding color
        cluster ratio metadata.
    """
    matching_result = _empty_matching_result()

    for index, user_image_url in enumerate(user_images_urls):
        loaded_image = load_image_from_url_with_requests(str(user_image_url))

        if loaded_image is None:
            continue

        matching_result["url"].append(str(user_image_url))
        matching_result["color_cluster_ratio"].append(
            _get_color_cluster_ratio(image_url_list, index)
        )

    return matching_result