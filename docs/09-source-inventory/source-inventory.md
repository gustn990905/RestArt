# Source Inventory

## 개요

이 문서는 RestArt 프로젝트에서 사용된 원본 코드, 기술 문서, 기획 문서, 발표 자료, 모델 자료, AR 자료를 기능별로 정리하기 위한 인벤토리 문서이다.

RestArt는 단일 기능 프로젝트가 아니라, AI 기반 작품 추천, 이미지 분석, 모바일 리플릿, 전시 추천, AR 작품 배치, 백엔드 API, DB 연동, 사업화 자료가 함께 구성된 통합 아트테크 플랫폼이다.

Day 8에서는 기존 자료를 단순히 파일 단위로 나열하는 것이 아니라, 각 자료가 어떤 기능과 연결되는지 정리한다.

---

## 정리 목적

Source Inventory의 목적은 다음과 같다.

1. 기존 프로젝트 자료를 빠짐없이 파악한다.
2. 원본 코드와 문서의 역할을 기록한다.
3. 기능별로 어떤 자료가 있는지 확인한다.
4. 이후 코드 정리, 문서화, README 작성 시 누락을 방지한다.
5. 포트폴리오에서 RestArt가 여러 기능을 포함한 통합 프로젝트임을 보여준다.

---

## 전체 자료 분류

RestArt 자료는 다음 범주로 나눈다.

| 분류                  | 설명                                                      |
| --------------------- | --------------------------------------------------------- |
| Backend Source        | FastAPI 기반 백엔드 API prototype 코드                    |
| Recommendation Source | 작품 추천, 색상 추출, 감성/색상 매칭 관련 코드            |
| Image Matching Source | 전시 촬영 이미지와 작품 이미지 매칭 관련 코드             |
| Leaflet Source        | 모바일 리플릿 생성, 대표 이미지 선정, 대표 색상 추출 코드 |
| Exhibition Source     | 근처 전시 추천, 랜덤 전시 추천, 전시 데이터 처리 코드     |
| Database Source       | 작품 DB loader, 추천 후보 작품 loader, SQL test schema    |
| Algorithm Documents   | 추천 알고리즘, 감성 테이블, 색상 테이블 설명 문서         |
| Business Documents    | 사업계획서, IR, 공모전 기획서, 발표자료                   |
| AR Source             | AR 작품 배치, Unity 또는 AR prototype 관련 자료           |
| Experiment Assets     | 인테리어 추천 실험, 모델 파일, notebook 자료              |
| Demo Assets           | 시연 흐름, 발표 이미지, 화면 캡처, 서비스 결과물          |

---

## 1. Backend Source

### 포함 자료

- `main4.py`
- `main.py`
- `exhibition.py`
- `recommend_picture.py`
- `spectral_image.py`
- `config.py`
- `.env.example`
- `requirements.txt`

### 현재 정리 위치

```text
apps/backend/api-prototype/
```

### 역할

Backend Source는 RestArt의 FastAPI prototype을 구성하는 자료이다.

주요 역할은 다음과 같다.

- 공간 이미지 기반 작품 추천 API
- 모바일 리플릿 생성 API
- 전시 추천 API
- 대표 RGB 분석 API
- 이미지 분석 API
- DB 설정 분리
- prototype 실행 환경 정리

---

## 2. Recommendation Source

### 포함 자료

- `image_utils.py`
- `recommend_picture.py`
- `signature_color.py`
- RestArt 색상표
- K-means 기반 대표 색상 추출 함수
- 색상 매칭 함수
- 작품 추천 후보 생성 로직

### 현재 정리 위치

```text
tools/recommendation-model/
```

### 현재 분리된 파일

```text
tools/recommendation-model/color_extraction/kmeans_color_extractor.py
tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
tools/recommendation-model/prototype/image_utils.py
```

### 역할

Recommendation Source는 RestArt의 작품 추천 로직을 구성한다.

주요 기능은 다음과 같다.

- 이미지 URL 로딩
- RGB 색상 추출
- K-means clustering
- 색상 비율 계산
- RestArt 색상표 매칭
- 리플릿 대표 색상 선정
- 추천 후보 작품 정렬을 위한 기초 데이터 생성

---

## 3. Image Matching Source

### 포함 자료

- `load_image_from_url_with_requests()`
- `restore_image()`
- `compare_images()`
- `find_best_matching_images()`
- `find_norm_images()`
- `align_images_akaze()`
- `align_images_orb2()`
- ORB / AKAZE 기반 feature matching 코드

### 현재 상태

현재 원본 image matching 로직은 `tools/recommendation-model/prototype/image_utils.py` 안에 포함되어 있다.

### 향후 정리 예정 위치

```text
tools/image-matching/
```

### 역할

Image Matching Source는 사용자가 전시장에서 촬영한 작품 이미지와 DB에 저장된 작품 이미지를 비교하는 기능과 연결된다.

주요 기능은 다음과 같다.

- 이미지 URL 로딩
- OpenCV 기반 이미지 전처리
- SSIM 기반 유사도 비교
- ORB 또는 AKAZE 기반 특징점 매칭
- 촬영 이미지와 전시 작품 이미지 매칭
- 모바일 리플릿 생성 전 작품 식별 보조

---

## 4. Leaflet Source

### 포함 자료

- `analyze_images_and_cluster()`
- `find_signiture_color()`
- `leaflet_design()`
- `gaussian_kernel()`
- `List1`
- `List2`
- `List3`
- `List4`

### 현재 정리 위치

```text
tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
```

### 역할

Leaflet Source는 사용자가 촬영한 작품 이미지를 기반으로 개인화 모바일 리플릿을 생성하는 기능과 연결된다.

주요 기능은 다음과 같다.

- 사용자가 촬영한 이미지 목록 처리
- 촬영 이미지 수가 부족한 경우 추천 후보 이미지 보충
- Spectral Clustering 기반 대표 이미지 선정
- 촬영 이미지들의 대표 색상 계산
- 대표 색상을 기반으로 리플릿 디자인 타입 결정

### 네이밍 메모

원본 prototype에서는 `find_signiture_color()`라는 함수명을 사용한다.

현재는 기존 코드 호환성을 위해 해당 함수명을 유지한다.

향후 전체 호출부를 확인한 뒤 `find_signature_color()`로 리팩터링할 수 있다.

---

## 5. Exhibition Source

### 포함 자료

- `random_exhibition()`
- `find_nearby_exhibitions()`
- `find1_nearby_exhibitions()`
- `exhibition.py`

### 현재 정리 위치

```text
apps/backend/api-prototype/exhibition.py
tools/recommendation-model/prototype/image_utils.py
```

### 향후 정리 예정 위치

```text
apps/backend/exhibition/
```

### 역할

Exhibition Source는 사용자의 위치 또는 리플릿 결과를 기반으로 전시를 추천하는 기능과 연결된다.

주요 기능은 다음과 같다.

- 랜덤 전시 추천
- 현재 위치 기반 근처 전시 추천
- 전시명, 전시 이미지, 시작일, 종료일 반환
- 리플릿 결과와 연결된 전시 추천

---

## 6. Database Source

### 포함 자료

- `artist_artwork_loader.py`
- `recommendation_artwork_loader.py`
- `schema.sql`
- `seed.example.sql`
- `config.py`
- `.env.example`

### 현재 정리 위치

```text
apps/backend/database/
apps/backend/api-prototype/config.py
```

### 역할

Database Source는 작품 데이터와 추천 후보 데이터를 backend prototype에서 다루기 위한 구조이다.

주요 기능은 다음과 같다.

- RestArt 작가 작품 DB 삽입
- 추천 후보 작품 데이터 삽입
- prototype SQL schema 정리
- 샘플 seed 데이터 작성
- DB 접속 정보를 환경변수 기반으로 분리

---

## 7. Algorithm Documents

### 포함 자료

- 알고리즘 문서화 자료
- 테이블 설명 자료
- 감성 테이블 설명
- 색상 테이블 설명
- K-means 기반 색상 추출 설명
- 켄달타우 추천 구조 설명

### 현재 정리 위치

```text
docs/05-database/
docs/06-architecture/
```

### 역할

Algorithm Documents는 RestArt 추천 시스템이 단순 이미지 비교가 아니라 색상, 감성, 작품 DB, 리플릿 데이터 흐름을 함께 사용하는 구조임을 설명한다.

주요 내용은 다음과 같다.

- 작품 DB 생성 과정
- 감성 추출 및 매핑 과정
- RGB 추출 과정
- K-means clustering
- RestArt 색상표 매핑
- 감성 일치 개수 기반 추천
- 켄달타우 기반 색상 순위 비교
- 모바일 리플릿 추천 로직

---

## 8. Business Documents

### 포함 자료

- 예비창업패키지 사업기획서
- 문화데이터 공모전 아이디어 기획서
- IR 발표자료
- 입주기업 연장평가 발표자료
- 사업계획서
- 발표자료 PDF

### 현재 상태

현재 business documents는 project background와 서비스 기획 근거 자료로 활용한다.

### 향후 정리 예정 위치

```text
docs/11-business/
docs/12-demo/
```

### 역할

Business Documents는 RestArt가 단순 기술 실험이 아니라 실제 사업화, 공모전, IR, 입주기업 평가 등과 연결된 프로젝트였음을 보여준다.

주요 활용 방식은 다음과 같다.

- 문제 정의
- 시장성
- 서비스 차별성
- 사용자 시나리오
- 수익 모델
- 발표 및 시연 흐름
- 사업화 가능성

---

## 9. AR Source

### 포함 자료

- AR 기능 관련 코드
- Unity 관련 자료
- 작품 배치 기능 자료
- AR prototype 또는 시연 자료

### 현재 상태

AR Source는 아직 별도 폴더로 정리되지 않았다.

### 향후 정리 예정 위치

```text
apps/ar-prototype/
docs/10-ar/
```

### 역할

AR Source는 RestArt가 추천한 작품을 실제 공간에 배치해볼 수 있는 기능과 연결된다.

주요 기능은 다음과 같다.

- 추천 작품을 AR 화면에 전달
- 실제 공간에서 작품 배치
- 작품 크기 및 위치 조정
- AR 미리보기
- 추천 결과와 AR 경험 연결

---

## 10. Experiment Assets

### 포함 자료

- `Deep_interior.ipynb`
- `rocom_model.h5`
- 인테리어 추천 관련 실험 자료
- 모델 실험 자료
- 색상 또는 이미지 분석 실험 자료

### 현재 상태

Experiment Assets는 아직 별도 실험 폴더로 정리되지 않았다.

### 향후 정리 예정 위치

```text
experiments/interior-recommendation/
```

### 역할

Experiment Assets는 인테리어 기반 작품 추천 또는 이미지 분석 모델의 실험 흔적을 보여준다.

주요 내용은 다음과 같다.

- 인테리어 이미지 분석 실험
- 모델 학습 또는 추론 실험
- 작품 추천 정확도 개선 시도
- 모델 파일 사용 기록
- notebook 기반 실험 과정

### 주의 사항

`rocom_model.h5`와 같은 모델 파일은 용량이 클 수 있으므로 GitHub에 직접 포함하기 전에 용량, 민감정보, 재현 가능성을 확인해야 한다.

---

## 11. Demo Assets

### 포함 자료

- 서비스 시연 흐름
- 발표자료 이미지
- 결과 화면
- 리플릿 결과 예시
- AR 시연 이미지
- 사업계획서 내 서비스 화면 자료

### 현재 상태

Demo Assets는 아직 최종 README와 연결되지 않았다.

### 향후 정리 예정 위치

```text
docs/12-demo/
assets/screenshots/
```

### 역할

Demo Assets는 GitHub 방문자가 RestArt의 실제 사용자 경험을 이해할 수 있도록 도와준다.

주요 활용 방식은 다음과 같다.

- 서비스 흐름 설명
- 사용자 시나리오 제시
- 추천 결과 예시
- 리플릿 결과 예시
- AR 배치 결과 예시
- 발표자료 기반 프로젝트 설명

---

## 현재까지 정리 완료된 영역

| 영역                        | 상태                                       |
| --------------------------- | ------------------------------------------ |
| Project Overview            | 완료                                       |
| Planning Documents          | 완료                                       |
| Requirements                | 완료                                       |
| Backend API Prototype       | 1차 정리 완료                              |
| Database Structure          | 1차 정리 완료                              |
| Recommendation Architecture | 완료                                       |
| Recommendation Model Code   | 일부 정리 완료                             |
| Source Inventory            | Day 8 정리 중                              |
| Image Matching              | 정리 예정                                  |
| Leaflet Feature             | 일부 코드 정리 완료, 서비스 문서 정리 예정 |
| Exhibition Recommendation   | 정리 예정                                  |
| AR Feature                  | 정리 예정                                  |
| Interior Experiment         | 정리 예정                                  |
| Business / IR Materials     | 정리 예정                                  |
| Final README                | 정리 예정                                  |

---

## 향후 정리 방향

Day 8 이후에는 이 인벤토리를 기준으로 다음 작업을 진행한다.

1. 이미지 매칭 코드를 별도 모듈로 분리한다.
2. 리플릿 기능을 backend service 구조로 정리한다.
3. 전시 추천 기능을 별도 모듈로 분리한다.
4. AR 기능 자료를 별도 폴더로 정리한다.
5. 인테리어 추천 실험 자료를 experiments 폴더에 정리한다.
6. 기획서, IR, 발표자료를 business/demo 문서로 요약한다.
7. 최종 README에서 전체 프로젝트 구조를 연결한다.
