"""
Image preprocessing utilities for the RestArt image matching module.

This module contains preprocessing logic separated from the initial
prototype image utility. The preprocessing step is used before image
similarity comparison or feature matching.
"""

from typing import Optional

import cv2
import numpy as np


def restore_image(image: Optional[np.ndarray]) -> Optional[np.ndarray]:
    """
    Apply a sharpening filter to an image.

    Parameters
    ----------
    image:
        OpenCV BGR image array.

    Returns
    -------
    Optional[np.ndarray]
        Sharpened OpenCV image if input is valid.
        None if the input image is None.
    """
    if image is None:
        return None

    sharpening_kernel = np.array(
        [
            [0, -1, 0],
            [-1, 5, -1],
            [0, -1, 0],
        ],
        dtype=np.float32,
    )

    restored_image = cv2.filter2D(image, -1, sharpening_kernel)
    return restored_image