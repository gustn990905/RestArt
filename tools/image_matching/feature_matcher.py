"""
Feature matching utilities for the RestArt image matching module.

This module contains AKAZE and ORB based feature matching logic
separated from the initial prototype image utility.
"""

from typing import Optional

import cv2
import numpy as np


def crop_center(image: np.ndarray, cropx: int, cropy: int) -> np.ndarray:
    """
    Crop the center area of an image.

    Parameters
    ----------
    image:
        OpenCV BGR image array.
    cropx:
        Target crop width.
    cropy:
        Target crop height.

    Returns
    -------
    np.ndarray
        Center-cropped image.
    """
    y, x, _ = image.shape
    startx = x // 2 - (cropx // 2)
    starty = y // 2 - (cropy // 2)
    return image[starty : starty + cropy, startx : startx + cropx]


def _ratio_test_matches(matches, ratio: float = 0.75) -> list:
    """
    Apply Lowe's ratio test to KNN matches.
    """
    good_matches = []

    for match_pair in matches:
        if len(match_pair) < 2:
            continue

        m, n = match_pair
        if m.distance < ratio * n.distance:
            good_matches.append(m)

    return good_matches


def align_images_akaze(
    img1: Optional[np.ndarray],
    img2: Optional[np.ndarray],
    max_features: int = 1000,
) -> int:
    """
    Match two images using AKAZE features.

    Parameters
    ----------
    img1:
        First OpenCV BGR image.
    img2:
        Second OpenCV BGR image.
    max_features:
        Kept for compatibility with the initial prototype function signature.

    Returns
    -------
    int
        Number of good matches if homography is valid.
        -1 if homography cannot be computed.
        -2 if there are not enough matches or descriptors are invalid.
    """
    if img1 is None or img2 is None:
        return -2

    img1_gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    akaze = cv2.AKAZE_create()
    keypoints1, descriptors1 = akaze.detectAndCompute(img1_gray, None)
    keypoints2, descriptors2 = akaze.detectAndCompute(img2_gray, None)

    if descriptors1 is None or descriptors2 is None:
        return -2

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = _ratio_test_matches(matches)

    min_match_count = 10
    if len(good_matches) > min_match_count:
        src_pts = np.float32(
            [keypoints1[m.queryIdx].pt for m in good_matches]
        ).reshape(-1, 1, 2)
        dst_pts = np.float32(
            [keypoints2[m.trainIdx].pt for m in good_matches]
        ).reshape(-1, 1, 2)

        homography_matrix, _ = cv2.findHomography(dst_pts, src_pts, cv2.RANSAC, 5.0)

        if homography_matrix is not None:
            return len(good_matches)

        return -1

    return -2


def align_images_orb2(
    descriptors1: Optional[np.ndarray],
    img2: Optional[np.ndarray],
    x_crop_ratio: float = 0.7,
    y_crop_ratio: float = 0.6,
) -> int:
    """
    Match precomputed ORB descriptors against a second image.

    Parameters
    ----------
    descriptors1:
        Precomputed ORB descriptors from the source image.
    img2:
        Target OpenCV BGR image.
    x_crop_ratio:
        Kept for compatibility with the initial prototype function signature.
    y_crop_ratio:
        Kept for compatibility with the initial prototype function signature.

    Returns
    -------
    int
        Number of good ORB matches.
        -2 if there are not enough matches or descriptors are invalid.
    """
    if descriptors1 is None or img2 is None:
        return -2

    img2_gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)

    orb = cv2.ORB_create()
    _, descriptors2 = orb.detectAndCompute(img2_gray, None)

    if descriptors2 is None:
        return -2

    bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=False)
    matches = bf.knnMatch(descriptors1, descriptors2, k=2)

    good_matches = _ratio_test_matches(matches)

    min_match_count = 10
    if len(good_matches) > min_match_count:
        return len(good_matches)

    return -2