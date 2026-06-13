"""
Image similarity utilities for the RestArt image matching module.

This module contains structural similarity comparison logic separated
from the initial prototype image utility.
"""

from typing import Optional

import cv2
import numpy as np
from skimage.metrics import structural_similarity as ssim


def compare_images(
    image_a: Optional[np.ndarray],
    image_b: Optional[np.ndarray],
    resize_to: tuple[int, int] = (300, 300),
) -> float:
    """
    Compare two images using structural similarity index measure.

    Parameters
    ----------
    image_a:
        First OpenCV BGR image.
    image_b:
        Second OpenCV BGR image.
    resize_to:
        Target size used before similarity comparison.

    Returns
    -------
    float
        Similarity score between 0.0 and 1.0.
        Returns 0.0 if either image is invalid.
    """
    if image_a is None or image_b is None:
        return 0.0

    try:
        resized_a = cv2.resize(image_a, resize_to)
        resized_b = cv2.resize(image_b, resize_to)

        gray_a = cv2.cvtColor(resized_a, cv2.COLOR_BGR2GRAY)
        gray_b = cv2.cvtColor(resized_b, cv2.COLOR_BGR2GRAY)

        score, _ = ssim(gray_a, gray_b, full=True)
        return float(score)

    except Exception as error:
        print(f"Error comparing images: {error}")
        return 0.0