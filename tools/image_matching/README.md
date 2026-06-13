# Image Matching Module

## Overview

The image matching module contains image loading, preprocessing, similarity comparison, and feature matching utilities used in the RestArt prototype.

This module is responsible for comparing user-captured artwork images with candidate artwork images stored in the artwork database or recommendation dataset.

The initial image utility included multiple responsibilities in a single file, including color extraction, leaflet image selection, exhibition recommendation, and image matching. The current module separates the image matching logic into smaller files so that each function group can be maintained independently.

---

## Module Structure

```text
tools/image_matching/
├─ __init__.py
├─ README.md
├─ image_loader.py
├─ image_preprocessing.py
├─ similarity.py
├─ feature_matcher.py
└─ matching_service.py
```

---

## File Responsibilities

| File                     | Responsibility                                              |
| ------------------------ | ----------------------------------------------------------- |
| `image_loader.py`        | Loads image URLs and converts them into OpenCV BGR arrays   |
| `image_preprocessing.py` | Applies image sharpening before comparison                  |
| `similarity.py`          | Compares two images using structural similarity             |
| `feature_matcher.py`     | Provides AKAZE and ORB based feature matching utilities     |
| `matching_service.py`    | Compares user-captured images with candidate artwork images |

---

## Main Functions

### Image Loading

| Function                              | Description                                                                                             |
| ------------------------------------- | ------------------------------------------------------------------------------------------------------- |
| `load_image_from_url_with_requests()` | Loads an image from a URL using `requests`, converts it to a PIL image, and returns an OpenCV BGR image |

---

### Image Preprocessing

| Function          | Description                                                    |
| ----------------- | -------------------------------------------------------------- |
| `restore_image()` | Applies a sharpening filter to an OpenCV image before matching |

---

### Similarity Comparison

| Function           | Description                                                                  |
| ------------------ | ---------------------------------------------------------------------------- |
| `compare_images()` | Resizes two images, converts them to grayscale, and compares them using SSIM |

---

### Feature Matching

| Function               | Description                                                 |
| ---------------------- | ----------------------------------------------------------- |
| `crop_center()`        | Crops the center region of an image                         |
| `align_images_akaze()` | Compares two images using AKAZE features                    |
| `align_images_orb2()`  | Compares precomputed ORB descriptors with a candidate image |

---

### Matching Service

| Function                       | Description                                                                   |
| ------------------------------ | ----------------------------------------------------------------------------- |
| `find_best_matching_images()`  | Finds the best matching candidate artwork images for user-captured image URLs |
| `find_best_matching_images2()` | Compatibility wrapper for prototype call sites                                |
| `find_norm_images()`           | Preserves lightweight prototype behavior for already-selected image URLs      |

---

## Matching Flow

The image matching flow is organized as follows.

```text
User-captured image URL
→ Load image from URL
→ Convert image to OpenCV BGR format
→ Extract ORB descriptors
→ Compare against candidate artwork images
→ Select the best matching candidate
→ Return matched image URL and color cluster metadata
```

For SSIM-based comparison, the flow is organized as follows.

```text
Image A
→ Resize
→ Convert to grayscale
→ Compare with Image B using SSIM
→ Return similarity score
```

---

## Return Convention

Some feature matching functions preserve the return convention used in the prototype implementation.

| Return value     | Meaning                                                          |
| ---------------- | ---------------------------------------------------------------- |
| Positive integer | Number of good feature matches                                   |
| `-1`             | Homography could not be computed                                 |
| `-2`             | Matching failed because descriptors or matches were insufficient |
| `0.0`            | Similarity comparison failed or invalid image input              |

---

## Dependencies

The module depends on the following Python libraries.

```text
opencv-python
numpy
requests
Pillow
scikit-image
```

These dependencies are already part of the backend and recommendation prototype environment.

---

## Current Scope

This module currently focuses on utility-level image matching logic.

Included scope:

- URL-based image loading
- Image sharpening
- SSIM comparison
- AKAZE feature matching
- ORB descriptor matching
- Candidate artwork matching service

Not included in this module:

- Backend API route implementation
- Database query implementation
- Image upload storage
- Recommendation ranking logic
- Mobile leaflet layout generation

---

## Planned Integration

The image matching module can be connected to the backend API flow as follows.

```text
Backend API
→ Receive user-captured image URLs
→ Load candidate artwork image URLs from database
→ Run image matching service
→ Return matched artwork candidates
→ Pass matched images to leaflet or recommendation flow
```

This separation allows the image matching logic to be reused by the mobile leaflet feature, exhibition artwork identification, and recommendation pipeline.
