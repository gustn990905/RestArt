# Feature Coverage Map

## 개요

이 문서는 RestArt 프로젝트의 주요 기능과 현재 보유한 코드·문서·자료의 대응 관계를 정리한다.

RestArt는 AI 기반 작품 추천, 색상 분석, 감성 매핑, 이미지 매칭, 모바일 리플릿, 전시 추천, AR 작품 배치, DB 연동, 사업화 자료가 함께 구성된 통합 아트테크 플랫폼이다.

Feature Coverage Map은 각 기능별로 다음 항목을 확인하기 위해 작성한다.

- 해당 기능이 프로젝트에 포함되어 있는지
- 관련 코드가 있는지
- 관련 문서가 있는지
- 현재 repository에 정리된 위치가 있는지
- 앞으로 추가 정리가 필요한지

---

## 기능 정리 기준

기능 상태는 다음 기준으로 구분한다.

| 상태                | 의미                                                      |
| ------------------- | --------------------------------------------------------- |
| Completed           | 기능 문서와 코드가 repository에 1차 정리됨                |
| Partially Organized | 원본 코드나 문서는 있으나 기능별 정리가 일부만 완료됨     |
| Planned             | 자료는 있으나 아직 repository 구조로 정리되지 않음        |
| Needs Review        | 파일 용량, 민감정보, 실행 가능성 등을 확인한 뒤 반영 필요 |

---

## 전체 기능 커버리지 요약

| 기능 영역                          | 관련 자료                           | 현재 상태           | 현재 위치                                                    | 향후 정리                                   |
| ---------------------------------- | ----------------------------------- | ------------------- | ------------------------------------------------------------ | ------------------------------------------- |
| Project Overview                   | 기획서, 사업계획서, 서비스 설명     | Completed           | `docs/00-overview/`, `docs/01-planning/`                     | 최종 README에 연결                          |
| Requirements                       | 기능 요구사항, MVP 범위             | Completed           | `docs/02-requirements/`                                      | 최종 README에 요약                          |
| Design Docs                        | 디자인/서비스 구조 자료             | Completed           | `docs/03-design/`                                            | 화면 흐름과 연결                            |
| Backend API Prototype              | FastAPI Python 코드                 | Partially Organized | `apps/backend/api-prototype/`                                | routes/services/schemas 구조 보강           |
| Database Structure                 | DB loader, SQL test schema          | Completed           | `apps/backend/database/`, `docs/05-database/`                | 실제 API 흐름과 연결                        |
| AI Recommendation Architecture     | 추천 알고리즘 문서                  | Completed           | `docs/06-architecture/`                                      | README 아키텍처 섹션에 연결                 |
| Recommendation Model Code          | 색상 추출, 리플릿 이미지 선정       | Partially Organized | `tools/recommendation-model/`                                | ranking utility 추가 검토                   |
| Image Matching                     | SSIM, ORB, AKAZE, 이미지 매칭       | Planned             | `tools/recommendation-model/prototype/image_utils.py`        | `tools/image-matching/`로 분리              |
| Mobile Leaflet                     | 대표 이미지, 대표 색상, 디자인 타입 | Partially Organized | `tools/recommendation-model/leaflet_generation/`             | backend leaflet service와 연결              |
| Exhibition Recommendation          | 근처 전시, 랜덤 전시 추천           | Planned             | `apps/backend/api-prototype/exhibition.py`, `image_utils.py` | `apps/backend/exhibition/`으로 분리         |
| AR Placement                       | AR 작품 배치, Unity 자료            | Planned             | 원본 자료 보유                                               | `apps/ar-prototype/`, `docs/10-ar/` 정리    |
| Interior Recommendation Experiment | notebook, model file                | Needs Review        | 원본 자료 보유                                               | `experiments/interior-recommendation/` 정리 |
| Business / IR Materials            | 사업계획서, IR, 공모전 자료         | Planned             | 원본 자료 보유                                               | `docs/11-business/`, `docs/12-demo/` 정리   |
| Demo Assets                        | 발표자료, 화면, 시연 흐름           | Planned             | 원본 자료 보유                                               | `docs/12-demo/`, `assets/screenshots/` 정리 |
| Final README                       | 전체 프로젝트 소개                  | Planned             | `README.md`                                                  | 최종 단계에서 작성                          |

---

## 1. Backend API 기능

### 기능 설명

Backend API는 RestArt의 추천, 리플릿, 전시 추천, 이미지 분석 기능을 외부 요청으로 실행하기 위한 FastAPI 기반 prototype이다.

### 포함 기능

- 공간 이미지 기반 작품 추천 API
- 전시 추천 API
- 리플릿 생성 API
- 대표 RGB 분석 API
- 이미지 비교 API
- DB 연결 설정

### 관련 코드

| 파일                   | 역할                                           |
| ---------------------- | ---------------------------------------------- |
| `main.py`              | FastAPI prototype 진입점                       |
| `main4.py`             | 기존 backend API prototype 원본                |
| `recommend_picture.py` | 공간 기반 추천 관련 코드                       |
| `exhibition.py`        | 전시 추천 관련 코드                            |
| `spectral_image.py`    | 이미지 분석 또는 spectral clustering 관련 코드 |
| `config.py`            | DB 환경변수 설정                               |
| `.env.example`         | 환경변수 예시                                  |
| `requirements.txt`     | backend 의존성 목록                            |

### 현재 상태

Partially Organized

### 현재 위치

```text
apps/backend/api-prototype/
```

### 향후 작업

- routes, services, schemas 폴더 구조 정리
- API endpoint별 요청/응답 구조 문서화
- 추천 모델 함수와 backend service 연결
- DB loader와 API 흐름 연결

---

## 2. 색상 추출 기능

### 기능 설명

색상 추출 기능은 이미지에서 대표 RGB와 색상 비율을 추출하고, RestArt 색상표와 매칭하는 기능이다.

### 포함 기능

- 이미지 URL 로딩
- RGB 이미지 변환
- K-means clustering
- 대표 색상 추출
- 색상 비율 계산
- RestArt 색상표 매칭

### 관련 코드

| 함수 또는 데이터        | 역할                           |
| ----------------------- | ------------------------------ |
| `RestArt_color`         | RestArt 자체 색상표            |
| `get_images_from_url()` | URL 기반 이미지 로딩           |
| `extract_top_colors()`  | K-means 기반 대표 색상 추출    |
| `colormatching()`       | RGB 값을 RestArt 색상명과 매칭 |

### 현재 상태

Completed

### 현재 위치

```text
tools/recommendation-model/color_extraction/kmeans_color_extractor.py
```

### 향후 작업

- 예외 처리 추가
- 이미지 요청 timeout 추가
- 색상 추출 결과 JSON schema 정리
- backend API와 연결

---

## 3. 감성 매핑 기능

### 기능 설명

감성 매핑 기능은 작품 이미지, 작품명, 작품 설명을 기반으로 작품 감성을 추출하고 RestArt 감성 카테고리에 매핑하는 기능이다.

### 포함 기능

- 작품 이미지 기반 감성 추론
- 작품 설명 기반 감성 추론
- RestArt 감성 테이블 매핑
- 작가 수정 감성 반영
- 추천 정렬 기준으로 감성 일치 개수 사용

### 관련 문서

| 문서                          | 역할                  |
| ----------------------------- | --------------------- |
| `emotion-mapping-pipeline.md` | 감성 매핑 처리 흐름   |
| `data-dictionary.md`          | 감성 테이블 구조      |
| `table-definition.md`         | 감성 관련 테이블 역할 |

### 현재 상태

Completed as architecture documentation

### 현재 위치

```text
docs/06-architecture/emotion-mapping-pipeline.md
docs/05-database/
```

### 향후 작업

- 실제 감성 추출 API 또는 모델 코드 확인
- 감성 태그 결과 예시 추가
- 작품 등록 API와 연결

---

## 4. 추천 정렬 기능

### 기능 설명

추천 정렬 기능은 감성 일치 개수와 켄달타우 점수를 기반으로 추천 작품의 순위를 결정하는 기능이다.

### 포함 기능

- 후보 작품 목록 생성
- 감성 일치 개수 계산
- 색상 순위 비교
- 켄달타우 점수 계산
- 추천 결과 정렬
- 추천 결과 저장

### 관련 문서

| 문서                          | 역할                     |
| ----------------------------- | ------------------------ |
| `similarity-ranking-logic.md` | 추천 정렬 기준 설명      |
| `recommendation-data-flow.md` | 추천 데이터 흐름 설명    |
| `database-overview.md`        | 추천 결과 저장 구조 설명 |

### 현재 상태

Partially Organized

### 현재 위치

```text
docs/06-architecture/similarity-ranking-logic.md
tools/recommendation-model/similarity/kendall_tau.py
```

### 향후 작업

- 기존 prototype에서 켄달타우 관련 코드 존재 여부 재확인
- 없으면 보완 작성 여부 결정
- `kendall_tau.py` 구현
- recommendation service와 연결

---

## 5. 이미지 매칭 기능

### 기능 설명

이미지 매칭 기능은 사용자가 촬영한 전시 작품 이미지와 DB에 저장된 작품 이미지를 비교하여 가장 유사한 작품을 찾는 기능이다.

### 포함 기능

- 이미지 URL 로딩
- OpenCV 이미지 변환
- 이미지 복원 필터
- SSIM 기반 유사도 비교
- ORB 기반 특징점 매칭
- AKAZE 기반 특징점 매칭
- 촬영 이미지와 전시 작품 이미지 매칭

### 관련 코드

| 함수                                  | 역할                             |
| ------------------------------------- | -------------------------------- |
| `load_image_from_url_with_requests()` | OpenCV용 이미지 로딩             |
| `restore_image()`                     | 이미지 샤프닝 필터 적용          |
| `compare_images()`                    | SSIM 기반 이미지 비교            |
| `find_best_matching_images()`         | 사용자 이미지와 작품 이미지 매칭 |
| `find_norm_images()`                  | normalized image mapping         |
| `align_images_akaze()`                | AKAZE 기반 특징점 매칭           |
| `align_images_orb2()`                 | ORB 기반 특징점 매칭             |

### 현재 상태

Planned

### 현재 위치

```text
tools/recommendation-model/prototype/image_utils.py
```

### 향후 정리 위치

```text
tools/image-matching/
```

### 향후 작업

- 이미지 로딩 함수 분리
- SSIM 비교 함수 분리
- ORB/AKAZE matcher 분리
- image matching README 작성
- 모바일 리플릿 기능과 연결

---

## 6. 모바일 리플릿 기능

### 기능 설명

모바일 리플릿 기능은 사용자가 전시장에서 촬영한 작품 이미지를 기반으로 개인화된 리플릿을 생성하는 기능이다.

### 포함 기능

- 촬영 이미지 목록 수집
- 촬영 이미지와 작품 DB 매칭
- Spectral Clustering 기반 대표 이미지 선정
- 대표 색상 추출
- 리플릿 디자인 타입 결정
- 추천 작품 또는 추천 전시 연결

### 관련 코드

| 함수 또는 데이터                   | 역할                                   |
| ---------------------------------- | -------------------------------------- |
| `gaussian_kernel()`                | RGB 유사도 계산용 kernel               |
| `analyze_images_and_cluster()`     | 촬영 이미지 대표 선정                  |
| `find_signiture_color()`           | 촬영 이미지 기반 대표 색상 추출        |
| `leaflet_design()`                 | 대표 색상 기반 리플릿 디자인 타입 결정 |
| `List1`, `List2`, `List3`, `List4` | 색상별 디자인 타입 분류                |

### 현재 상태

Partially Organized

### 현재 위치

```text
tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
docs/06-architecture/leaflet-recommendation-logic.md
```

### 향후 작업

- backend leaflet service 작성
- 리플릿 API 흐름 정리
- 리플릿 결과 구조 문서화
- 전시 추천 기능과 연결
- 데모 시나리오 작성

---

## 7. 전시 추천 기능

### 기능 설명

전시 추천 기능은 사용자의 위치 또는 리플릿 결과를 기반으로 가까운 전시 또는 관련 전시를 추천하는 기능이다.

### 포함 기능

- 랜덤 전시 추천
- 위치 기반 근처 전시 추천
- 하버사인 거리 기반 계산
- 유클리드 거리 기반 계산
- 전시명, 전시 이미지, 전시 기간 반환

### 관련 코드

| 함수                         | 역할                              |
| ---------------------------- | --------------------------------- |
| `random_exhibition()`        | 전시 목록에서 랜덤 전시 선택      |
| `find1_nearby_exhibitions()` | 하버사인 거리 기반 근처 전시 탐색 |
| `find_nearby_exhibitions()`  | 유클리드 거리 기반 근처 전시 탐색 |
| `exhibition.py`              | 전시 API 또는 전시 데이터 처리    |

### 현재 상태

Planned

### 현재 위치

```text
apps/backend/api-prototype/exhibition.py
tools/recommendation-model/prototype/image_utils.py
```

### 향후 정리 위치

```text
apps/backend/exhibition/
docs/09-exhibition/
```

### 향후 작업

- 전시 추천 서비스 파일 생성
- 거리 계산 방식 차이 문서화
- 모바일 리플릿 전시 추천과 연결
- API route와 연결

---

## 8. AR 작품 배치 기능

### 기능 설명

AR 작품 배치 기능은 추천된 작품을 실제 공간에 배치해볼 수 있도록 하는 기능이다.

### 포함 기능

- 추천 작품 선택
- AR 화면으로 작품 데이터 전달
- 실제 공간에서 작품 배치
- 작품 크기 및 위치 조정
- 공간 이미지 기반 추천과 AR 경험 연결

### 관련 자료

- AR 코드
- Unity 관련 자료
- AR prototype 자료
- AR 기능 설명 문서
- 발표자료 내 AR 기능 이미지

### 현재 상태

Planned

### 향후 정리 위치

```text
apps/ar-prototype/
docs/10-ar/
```

### 향후 작업

- AR 기능 개요 문서 작성
- Unity 구조 정리
- 핵심 script 선별
- AR demo scenario 작성
- README에서 AR 기능 연결

---

## 9. 인테리어 추천 실험 기능

### 기능 설명

인테리어 추천 실험 기능은 사용자의 공간 이미지와 인테리어 이미지 또는 모델 결과를 바탕으로 어울리는 작품을 추천하는 실험 기능이다.

### 포함 자료

- `Deep_interior.ipynb`
- `rocom_model.h5`
- 인테리어 추천 관련 문서
- 모델 실험 자료

### 현재 상태

Needs Review

### 향후 정리 위치

```text
experiments/interior-recommendation/
```

### 향후 작업

- notebook 파일 정리
- 모델 파일 용량 확인
- 모델 파일 직접 포함 여부 결정
- 실험 목적과 입력/출력 문서화
- 추천 모델과의 연결 관계 설명

---

## 10. 사업화 및 발표 자료

### 기능 설명

사업화 및 발표 자료는 RestArt가 실제 공모전, IR, 예비창업패키지, 입주기업 평가와 연결된 프로젝트였음을 보여주는 근거 자료이다.

### 포함 자료

- 예비창업패키지 선정 사업기획서
- 문화데이터 공모전 대상 아이디어 기획서
- RestArt 사업계획서
- IR 발표자료
- 입주기업 연장평가 발표자료
- 알고리즘 문서화 자료
- 테이블 설명 자료

### 현재 상태

Planned

### 향후 정리 위치

```text
docs/11-business/
docs/12-demo/
```

### 향후 작업

- 사업 개요 요약
- 문제 정의 및 솔루션 정리
- 서비스 경쟁력 정리
- 수익 모델 정리
- 시연 흐름 정리
- 발표자료 기반 demo scenario 작성

---

## 기능별 다음 작업 우선순위

| 우선순위 | 기능                | 다음 작업                           |
| -------- | ------------------- | ----------------------------------- |
| 1        | Image Matching      | `tools/image-matching/`로 코드 분리 |
| 2        | Backend API         | routes/services/schemas 구조 정리   |
| 3        | Leaflet             | backend leaflet service 정리        |
| 4        | Exhibition          | 전시 추천 service 분리              |
| 5        | AR                  | AR prototype 자료 정리              |
| 6        | Interior Experiment | notebook/model 자료 검토            |
| 7        | Business / Demo     | 기획서 및 발표자료 요약             |
| 8        | README              | 전체 기능 연결                      |

---

## 정리

RestArt는 기능이 많은 프로젝트이므로, 단순히 하나의 backend repository처럼 보이게 정리하는 것보다 기능별 coverage를 명확히 보여주는 것이 중요하다.

이 문서는 이후 작업에서 어떤 기능이 이미 정리되었고, 어떤 기능을 추가로 정리해야 하는지 확인하는 기준으로 사용한다.
