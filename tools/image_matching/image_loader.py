"""
Image loading utilities for the RestArt image matching module.

This module contains image loading logic separated from the initial
prototype image utility. The loaded image is returned as an OpenCV BGR
NumPy array so that it can be used directly by similarity comparison
and feature matching functions.
"""

from io import BytesIO
from typing import Optional

import cv2
import numpy as np
import requests
from PIL import Image


def load_image_from_url_with_requests(url: str, timeout: int = 10) -> Optional[np.ndarray]:
    """
    Load an image from a URL and convert it into an OpenCV BGR image.

    Parameters
    ----------
    url:
        Image URL to load.
    timeout:
        Request timeout in seconds.

    Returns
    -------
    Optional[np.ndarray]
        OpenCV BGR image array if loading succeeds.
        None if loading fails.
    """
    try:
        response = requests.get(url, timeout=timeout)
        response.raise_for_status()

        image = Image.open(BytesIO(response.content))
        image = image.convert("RGBA")
        np_image = np.array(image)

        if np_image.shape[2] == 4:
            return cv2.cvtColor(np_image, cv2.COLOR_RGBA2BGR)

        return cv2.cvtColor(np_image, cv2.COLOR_RGB2BGR)

    except Exception as error:
        print(f"Error loading image from {url}: {error}")
        return None
    