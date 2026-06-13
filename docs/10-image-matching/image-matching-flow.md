# Image Matching Flow

## 개요

Image Matching Flow는 사용자가 전시장에서 촬영한 작품 이미지와 후보 작품 이미지 데이터를 비교하여 가장 유사한 작품을 찾는 흐름이다.

RestArt의 이미지 매칭 기능은 모바일 리플릿 생성, 전시 작품 식별, 작품 추천 결과 보정에 활용될 수 있다.

초기 prototype에서는 이미지 로딩, 전처리, SSIM 비교, ORB/AKAZE 기반 feature matching 로직이 하나의 utility 파일 안에 함께 포함되어 있었다. 현재 구조에서는 이미지 매칭 관련 로직을 `tools/image_matching/` 모듈로 분리한다.

---

## 목적

Image Matching Flow의 목적은 다음과 같다.

1. 사용자 촬영 이미지와 후보 작품 이미지를 비교한다.
2. 전시장에서 촬영한 이미지가 어떤 작품과 가장 유사한지 판단한다.
3. 매칭된 작품 이미지 URL과 색상 cluster metadata를 반환한다.
4. 모바일 리플릿 생성 또는 추천 pipeline의 입력값으로 사용할 수 있도록 한다.
5. 이미지 비교 로직을 backend API, leaflet 기능, recommendation 기능에서 재사용할 수 있도록 분리한다.

---

## 모듈 구조

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

## 파일별 역할

| 파일                     | 역할                                                                |
| ------------------------ | ------------------------------------------------------------------- |
| `image_loader.py`        | URL 기반 이미지를 불러와 OpenCV BGR image로 변환                    |
| `image_preprocessing.py` | 이미지 비교 전 sharpening filter 적용                               |
| `similarity.py`          | SSIM 기반 이미지 유사도 비교                                        |
| `feature_matcher.py`     | AKAZE / ORB 기반 특징점 매칭                                        |
| `matching_service.py`    | 사용자 촬영 이미지와 후보 작품 이미지 목록을 비교하는 service layer |

---

## 전체 처리 흐름

```text
User-captured image URLs
→ Candidate artwork image URLs
→ Load images from URL
→ Convert images to OpenCV BGR format
→ Extract ORB descriptors from user images
→ Compare descriptors with candidate artwork images
→ Select best matched candidate image
→ Return matched image URL and color cluster metadata
```

---

## 1. Image Loading

### 대상 파일

```text
tools/image_matching/image_loader.py
```

### 주요 함수

```text
load_image_from_url_with_requests()
```

### 역할

이미지 URL을 입력받아 HTTP 요청으로 이미지를 불러오고, PIL Image를 거쳐 OpenCV에서 사용할 수 있는 BGR image array로 변환한다.

### 입력

```text
image URL
```

### 출력

```text
OpenCV BGR image array
```

### 처리 흐름

```text
URL
→ requests.get()
→ PIL Image
→ RGBA conversion
→ NumPy array
→ OpenCV BGR image
```

---

## 2. Image Preprocessing

### 대상 파일

```text
tools/image_matching/image_preprocessing.py
```

### 주요 함수

```text
restore_image()
```

### 역할

이미지 비교 전에 sharpening filter를 적용하여 이미지의 경계와 특징을 강화한다.

### 입력

```text
OpenCV BGR image
```

### 출력

```text
Sharpened OpenCV BGR image
```

### 처리 흐름

```text
OpenCV image
→ sharpening kernel 적용
→ restored image 반환
```

---

## 3. SSIM Similarity Comparison

### 대상 파일

```text
tools/image_matching/similarity.py
```

### 주요 함수

```text
compare_images()
```

### 역할

두 이미지를 같은 크기로 조정한 뒤 grayscale로 변환하고, SSIM을 사용하여 구조적 유사도를 계산한다.

### 입력

```text
image_a
image_b
resize size
```

### 출력

```text
similarity score
```

### 처리 흐름

```text
Image A / Image B
→ Resize
→ Convert to grayscale
→ SSIM comparison
→ Similarity score 반환
```

### 반환 기준

| 반환값      | 의미                                    |
| ----------- | --------------------------------------- |
| `0.0 ~ 1.0` | 두 이미지의 구조적 유사도               |
| `0.0`       | 이미지 입력이 유효하지 않거나 비교 실패 |

---

## 4. Feature Matching

### 대상 파일

```text
tools/image_matching/feature_matcher.py
```

### 주요 함수

```text
crop_center()
align_images_akaze()
align_images_orb2()
```

### 역할

Feature Matching은 이미지의 특징점을 추출하고, 두 이미지 간의 특징점 매칭 정도를 계산한다.

RestArt prototype에서는 AKAZE와 ORB 기반 매칭을 사용한다.

---

### 4.1 AKAZE Matching

#### 함수

```text
align_images_akaze()
```

#### 처리 흐름

```text
Image A / Image B
→ Convert to grayscale
→ AKAZE keypoint detection
→ Descriptor extraction
→ BFMatcher + Hamming distance
→ Lowe ratio test
→ Homography validation
→ Good match count 반환
```

#### 반환 기준

| 반환값       | 의미                                    |
| ------------ | --------------------------------------- |
| 양수 integer | good match 개수                         |
| `-1`         | homography 계산 실패                    |
| `-2`         | descriptor가 없거나 충분한 match가 없음 |

---

### 4.2 ORB Matching

#### 함수

```text
align_images_orb2()
```

#### 처리 흐름

```text
User image descriptors
→ Candidate image
→ Candidate image grayscale conversion
→ ORB descriptor extraction
→ BFMatcher + Hamming distance
→ Lowe ratio test
→ Good match count 반환
```

#### 반환 기준

| 반환값       | 의미                                    |
| ------------ | --------------------------------------- |
| 양수 integer | good match 개수                         |
| `-2`         | descriptor가 없거나 충분한 match가 없음 |

---

## 5. Matching Service

### 대상 파일

```text
tools/image_matching/matching_service.py
```

### 주요 함수

```text
find_best_matching_images()
find_best_matching_images2()
find_norm_images()
```

---

### 5.1 `find_best_matching_images()`

#### 역할

사용자 촬영 이미지 목록과 후보 작품 이미지 목록을 비교하여 가장 유사한 후보 작품 이미지를 찾는다.

#### 입력

```text
user_images_urls
image_url_list
similarity_threshold
```

#### `image_url_list` 예상 구조

```text
{
  "url": [...],
  "color_cluster_ratio": [...]
}
```

#### 출력

```text
{
  "url": [...],
  "color_cluster_ratio": [...]
}
```

#### 처리 흐름

```text
Candidate artwork image URLs 로딩
→ User-captured image URLs 로딩
→ User image ORB descriptor 추출
→ Candidate artwork image와 ORB feature matching
→ 가장 높은 matching score를 가진 후보 선택
→ threshold 이상인 경우 결과에 추가
→ matched URL과 color_cluster_ratio 반환
```

---

### 5.2 `find_best_matching_images2()`

#### 역할

초기 prototype의 호출부와 호환성을 유지하기 위한 wrapper 함수이다.

내부적으로는 `find_best_matching_images()`를 호출한다.

---

### 5.3 `find_norm_images()`

#### 역할

이미 선택된 사용자 이미지 URL을 그대로 유지하면서, 순서에 맞는 color cluster metadata를 연결한다.

이 함수는 lightweight prototype behavior를 유지하기 위한 함수이다.

---

## Backend Integration Flow

Image Matching Module은 backend API와 다음 흐름으로 연결될 수 있다.

```text
Backend API request
→ user image URLs 수신
→ candidate artwork image URLs 조회
→ image matching service 실행
→ matched artwork image URLs 반환
→ leaflet generation 또는 recommendation service로 전달
```

---

## Mobile Leaflet 연결

모바일 리플릿 기능과 연결될 경우 흐름은 다음과 같다.

```text
User-captured artwork images
→ Image matching
→ Matched artwork candidates
→ Representative image selection
→ Signature color extraction
→ Leaflet design type selection
→ Mobile leaflet result
```

---

## Recommendation 연결

작품 추천 기능과 연결될 경우 흐름은 다음과 같다.

```text
User space image
→ Color extraction
→ Emotion / color-based recommendation
→ Candidate artwork list
→ Image matching validation
→ Final recommendation result
```

---

## Error Handling 기준

Image Matching Module은 prototype 호환성을 유지하면서 다음 방식으로 오류 상황을 처리한다.

| 상황                   | 처리                        |
| ---------------------- | --------------------------- |
| image URL loading 실패 | 해당 image 제외             |
| image가 `None`인 경우  | 비교하지 않고 skip          |
| descriptor 추출 실패   | matching score `-2` 처리    |
| match 개수 부족        | matching score `-2` 처리    |
| homography 실패        | matching score `-1` 처리    |
| SSIM 비교 실패         | similarity score `0.0` 처리 |

---

## 현재 범위

현재 Image Matching Module은 utility-level 기능 분리를 목표로 한다.

포함 범위:

- URL image loading
- image preprocessing
- SSIM similarity comparison
- AKAZE feature matching
- ORB feature matching
- candidate artwork matching service

제외 범위:

- backend route 구현
- database query 구현
- image upload storage 구현
- recommendation ranking 구현
- leaflet layout rendering 구현

---

## 후속 구현 방향

후속 구현 단계에서는 다음 작업을 진행할 수 있다.

1. backend API route와 `matching_service.py` 연결
2. DB에서 후보 작품 이미지 URL을 조회하는 repository layer 추가
3. matching 결과에 artwork id, title, artist metadata 추가
4. threshold 기준 실험 및 조정
5. mobile leaflet service와 직접 연결
6. image upload storage 또는 object storage 연동
7. 실패 image URL logging 구조 추가
