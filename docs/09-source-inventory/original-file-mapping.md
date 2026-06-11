# Original File Mapping

## 개요

이 문서는 RestArt 프로젝트의 기존 prototype 파일이 현재 repository 구조에서 어떤 기능 모듈로 분리되었는지 기록한다.

초기 prototype 단계에서는 백엔드 API, 이미지 분석, 색상 추출, 모바일 리플릿, 전시 추천 로직이 일부 파일에 함께 포함되어 있었다.

현재 repository에서는 각 기능의 역할을 명확히 하기 위해 기존 파일을 기능 단위로 재배치하고, 핵심 로직을 별도 모듈로 분리한다.

---

## 정리 기준

기존 파일은 다음 기준으로 재배치한다.

| 기준      | 설명                                                                            |
| --------- | ------------------------------------------------------------------------------- |
| 원본 유지 | 기존 prototype의 핵심 함수명과 동작 흐름은 가능한 유지                          |
| 기능 분리 | 하나의 파일에 섞여 있던 기능을 추천, 리플릿, 이미지 매칭, 전시 추천 등으로 분리 |
| 구조화    | 유지보수를 고려하여 기능별 폴더와 README 구성                                   |
| 보류      | 모델 파일, 대용량 자료, 실행 환경 의존 파일은 검토 후 반영                      |
| 제외      | key, pem, cache, IDE 설정 등 repository에 부적절한 파일 제외                    |

---

## 1. Backend API 파일 매핑

| 기존 파일              | 현재 위치                                         | 상태      | 역할                                  |
| ---------------------- | ------------------------------------------------- | --------- | ------------------------------------- |
| `main4.py`             | `apps/backend/api-prototype/main.py`              | 반영 완료 | FastAPI prototype 진입점              |
| `main.py`              | `apps/backend/api-prototype/main.py` 참고         | 반영 완료 | API prototype 구조 참고               |
| `exhibition.py`        | `apps/backend/api-prototype/exhibition.py`        | 반영 완료 | 전시 추천 및 전시 데이터 처리         |
| `recommend_picture.py` | `apps/backend/api-prototype/recommend_picture.py` | 반영 완료 | 공간 이미지 기반 작품 추천            |
| `spectral_image.py`    | `apps/backend/api-prototype/spectral_image.py`    | 반영 완료 | 이미지 분석 및 clustering 관련 처리   |
| `config.py`            | `apps/backend/api-prototype/config.py`            | 반영 완료 | DB 접속 설정을 환경변수 기반으로 분리 |
| `.env.example`         | `apps/backend/api-prototype/.env.example`         | 반영 완료 | 실제 비밀값 없이 환경변수 예시 제공   |
| `requirements.txt`     | `apps/backend/api-prototype/requirements.txt`     | 반영 완료 | backend prototype 실행 의존성 정리    |

---

## 2. Recommendation / Image Utility 파일 매핑

| 기존 파일              | 현재 위치                                             | 상태        | 역할                                                             |
| ---------------------- | ----------------------------------------------------- | ----------- | ---------------------------------------------------------------- |
| `image_utils.py`       | `tools/recommendation-model/prototype/image_utils.py` | 원본 보존   | 이미지 분석, 색상 추출, 이미지 매칭, 리플릿, 전시 추천 로직 포함 |
| `mkapi/image_utils.py` | `tools/recommendation-model/prototype/image_utils.py` | 원본 보존   | recommendation prototype utility                                 |
| `signiture_color.py`   | `apps/backend/api-prototype/signature_color.py`       | 파일명 정리 | 색상 관련 prototype 코드                                         |
| `recommend_picture.py` | `apps/backend/api-prototype/recommend_picture.py`     | 반영 완료   | 추천 API와 공간 기반 작품 추천 흐름 참고                         |

---

## 3. 색상 추출 코드 매핑

기존 `image_utils.py`에 포함되어 있던 색상 추출 로직은 recommendation model의 색상 추출 모듈로 분리하였다.

| 기존 코드 요소          | 현재 위치                                                               | 상태      | 역할                           |
| ----------------------- | ----------------------------------------------------------------------- | --------- | ------------------------------ |
| `RestArt_color`         | `tools/recommendation-model/color_extraction/kmeans_color_extractor.py` | 분리 완료 | RestArt 자체 색상표            |
| `get_images_from_url()` | `tools/recommendation-model/color_extraction/kmeans_color_extractor.py` | 분리 완료 | URL 기반 이미지 로딩           |
| `extract_top_colors()`  | `tools/recommendation-model/color_extraction/kmeans_color_extractor.py` | 분리 완료 | K-means 기반 대표 색상 추출    |
| `colormatching()`       | `tools/recommendation-model/color_extraction/kmeans_color_extractor.py` | 분리 완료 | 추출 RGB와 RestArt 색상표 매칭 |

---

## 4. 모바일 리플릿 코드 매핑

기존 `image_utils.py`의 리플릿 관련 로직은 `leaflet_generation` 모듈로 분리하였다.

| 기존 코드 요소                     | 현재 위치                                                                 | 상태      | 역할                                   |
| ---------------------------------- | ------------------------------------------------------------------------- | --------- | -------------------------------------- |
| `gaussian_kernel()`                | `tools/recommendation-model/leaflet_generation/leaflet_image_selector.py` | 분리 완료 | RGB 유사도 계산                        |
| `analyze_images_and_cluster()`     | `tools/recommendation-model/leaflet_generation/leaflet_image_selector.py` | 분리 완료 | 촬영 이미지 중 대표 이미지 선정        |
| `find_signiture_color()`           | `tools/recommendation-model/leaflet_generation/leaflet_image_selector.py` | 분리 완료 | 촬영 이미지 기반 대표 색상 추출        |
| `leaflet_design()`                 | `tools/recommendation-model/leaflet_generation/leaflet_image_selector.py` | 분리 완료 | 대표 색상 기반 리플릿 디자인 타입 결정 |
| `List1`, `List2`, `List3`, `List4` | `tools/recommendation-model/leaflet_generation/leaflet_image_selector.py` | 분리 완료 | 색상별 리플릿 디자인 그룹              |

### 네이밍 메모

초기 prototype에서는 `find_signiture_color()`라는 함수명을 사용한다.

현재 단계에서는 기존 코드와의 호환성을 우선하여 함수명을 유지한다.
향후 전체 호출부를 확인한 뒤 `find_signature_color()`로 리팩터링할 수 있다.

---

## 5. 이미지 매칭 코드 매핑

이미지 매칭 관련 로직은 현재 원본 utility에 보존되어 있으며, 후속 구현 단계에서 `tools/image-matching/`으로 분리한다.

| 기존 코드 요소                        | 현재 위치                                             | 후속 정리 위치                                | 상태      |
| ------------------------------------- | ----------------------------------------------------- | --------------------------------------------- | --------- |
| `load_image_from_url_with_requests()` | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/image_loader.py`        | 분리 예정 |
| `restore_image()`                     | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/image_preprocessing.py` | 분리 예정 |
| `compare_images()`                    | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/similarity.py`          | 분리 예정 |
| `find_best_matching_images()`         | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/matching_service.py`    | 분리 예정 |
| `find_norm_images()`                  | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/matching_service.py`    | 분리 예정 |
| `align_images_akaze()`                | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/feature_matcher.py`     | 분리 예정 |
| `align_images_orb2()`                 | `tools/recommendation-model/prototype/image_utils.py` | `tools/image-matching/feature_matcher.py`     | 분리 예정 |

이미지 매칭 로직은 전시장에서 촬영한 작품 이미지와 DB 작품 이미지를 비교하는 기능과 연결된다. 원본 `image_utils.py`에는 색상 추출, 리플릿, 전시 추천, ORB/AKAZE 기반 매칭 로직이 함께 포함되어 있다.

---

## 6. 전시 추천 코드 매핑

전시 추천 관련 로직은 현재 backend prototype과 image utility에 분산되어 있으며, 후속 구현 단계에서 exhibition module로 분리한다.

| 기존 코드 요소               | 현재 위치                                             | 후속 정리 위치                                  | 상태      |
| ---------------------------- | ----------------------------------------------------- | ----------------------------------------------- | --------- |
| `random_exhibition()`        | `tools/recommendation-model/prototype/image_utils.py` | `apps/backend/exhibition/exhibition_service.py` | 분리 예정 |
| `find1_nearby_exhibitions()` | `tools/recommendation-model/prototype/image_utils.py` | `apps/backend/exhibition/nearby_exhibition.py`  | 분리 예정 |
| `find_nearby_exhibitions()`  | `tools/recommendation-model/prototype/image_utils.py` | `apps/backend/exhibition/nearby_exhibition.py`  | 분리 예정 |
| `exhibition.py`              | `apps/backend/api-prototype/exhibition.py`            | `apps/backend/exhibition/`                      | 분리 예정 |

---

## 7. Database 파일 매핑

| 기존 파일 또는 구조             | 현재 위치                                                | 상태                  | 역할                                 |
| ------------------------------- | -------------------------------------------------------- | --------------------- | ------------------------------------ |
| `restartdb.py`                  | `apps/backend/database/artist_artwork_loader.py`         | 반영 완료             | RestArt 작가 작품 DB 삽입 코드       |
| `images.py`                     | `apps/backend/database/recommendation_artwork_loader.py` | 반영 완료             | 추천 후보 작품 데이터 삽입 코드      |
| 기존 `images` table insert 구조 | `apps/backend/database/schema.sql`                       | test schema 정리 완료 | prototype 테스트용 SQL schema로 확장 |
| sample seed data                | `apps/backend/database/seed.example.sql`                 | 반영 완료             | 비민감 예시 데이터 삽입 SQL          |

---

## 8. 알고리즘 / 테이블 문서 매핑

| 기존 자료            | 현재 위치                                           | 상태        | 역할                                                         |
| -------------------- | --------------------------------------------------- | ----------- | ------------------------------------------------------------ |
| 알고리즘 문서화 자료 | `docs/06-architecture/`                             | 문서화 완료 | 색상 추출, 감성 매핑, 추천 정렬, 리플릿 추천 흐름 정리       |
| 테이블 설명 자료     | `docs/05-database/`                                 | 문서화 완료 | DB table definition, data dictionary, SQL test schema에 반영 |
| 감성 테이블 설명     | `docs/06-architecture/emotion-mapping-pipeline.md`  | 문서화 완료 | RestArt 감성 매핑 구조 정리                                  |
| 색상 테이블 설명     | `docs/06-architecture/color-extraction-pipeline.md` | 문서화 완료 | RestArt 색상표 및 RGB 추출 구조 정리                         |
| 켄달타우 추천 설명   | `docs/06-architecture/similarity-ranking-logic.md`  | 문서화 완료 | 추천 정렬 로직으로 정리                                      |

---

## 9. Business / IR / Planning 자료 매핑

| 기존 자료                         | 후속 정리 위치                                   | 상태      | 역할                              |
| --------------------------------- | ------------------------------------------------ | --------- | --------------------------------- |
| 예비창업패키지 선정 사업기획서    | `docs/11-business/business-overview.md`          | 정리 예정 | 사업 배경, 문제 정의, 솔루션 근거 |
| 문화데이터 공모전 아이디어 기획서 | `docs/11-business/competition-and-ir-summary.md` | 정리 예정 | 공모전 아이디어 및 서비스 경쟁력  |
| RestArt 사업계획서                | `docs/11-business/service-strategy.md`           | 정리 예정 | 서비스 전략, 수익 모델, 시장성    |
| IR 발표자료                       | `docs/12-demo/presentation-summary.md`           | 정리 예정 | 발표 흐름 및 핵심 메시지          |
| 입주기업 연장평가 발표자료        | `docs/12-demo/presentation-summary.md`           | 정리 예정 | 사업화 및 운영 성과 자료          |
| 서비스 화면 또는 시연 자료        | `docs/12-demo/service-demo-flow.md`              | 정리 예정 | 사용자 시나리오 및 데모 흐름      |

---

## 10. AR 자료 매핑

| 기존 자료       | 후속 정리 위치                         | 상태      | 역할                                  |
| --------------- | -------------------------------------- | --------- | ------------------------------------- |
| AR 기능 코드    | `apps/ar-prototype/scripts/`           | 정리 예정 | Unity 또는 AR 기능 핵심 script 선별   |
| AR 기능 문서    | `docs/10-ar/ar-feature-overview.md`    | 정리 예정 | AR 작품 배치 기능 개요                |
| AR 배치 흐름    | `docs/10-ar/ar-placement-flow.md`      | 정리 예정 | 추천 작품을 AR 화면으로 전달하는 흐름 |
| AR 시연 자료    | `docs/10-ar/ar-demo-scenario.md`       | 정리 예정 | AR demo 설명                          |
| Unity 구조 자료 | `apps/ar-prototype/unity-structure.md` | 정리 예정 | Unity 프로젝트 구조 설명              |

Unity 프로젝트 전체를 그대로 포함하면 repository가 과도하게 무거워질 수 있으므로, 핵심 script와 구조 문서를 우선 정리한다.

---

## 11. Experiment / Model 자료 매핑

| 기존 자료                       | 후속 정리 위치                                                      | 상태      | 역할                                       |
| ------------------------------- | ------------------------------------------------------------------- | --------- | ------------------------------------------ |
| `Deep_interior.ipynb`           | `experiments/interior-recommendation/Deep_interior.ipynb`           | 검토 예정 | 인테리어 기반 작품 추천 실험 notebook      |
| `rocom_model.h5`                | `experiments/interior-recommendation/model-notes.md` 또는 별도 저장 | 검토 필요 | 모델 파일은 용량과 GitHub 적합성 확인 필요 |
| 인테리어 추천 문서              | `experiments/interior-recommendation/README.md`                     | 정리 예정 | 실험 목적과 입력/출력 정리                 |
| 색상 또는 이미지 분석 실험 자료 | `experiments/interior-recommendation/assets/`                       | 검토 예정 | 실험 보조 자료                             |

---

## 12. Demo / Screenshot 자료 매핑

| 기존 자료               | 후속 정리 위치                      | 상태      | 역할                      |
| ----------------------- | ----------------------------------- | --------- | ------------------------- |
| 서비스 시연 이미지      | `assets/screenshots/`               | 정리 예정 | README와 demo 문서에 활용 |
| 발표자료 내 화면 자료   | `docs/12-demo/screenshots/`         | 정리 예정 | 프로젝트 흐름 설명에 활용 |
| 리플릿 결과 이미지      | `docs/12-demo/leaflet-results/`     | 정리 예정 | 모바일 리플릿 기능 시연   |
| AR 배치 결과 이미지     | `docs/10-ar/demo-assets/`           | 정리 예정 | AR 작품 배치 기능 시연    |
| 전체 서비스 흐름 이미지 | `docs/12-demo/service-demo-flow.md` | 정리 예정 | 최종 README 연결          |

---

## 13. 제외 또는 보류 파일 기준

다음 파일은 repository에 직접 포함하지 않는다.

| 파일 유형              | 처리 방식          | 이유                                 |
| ---------------------- | ------------------ | ------------------------------------ |
| `.pem`                 | 제외               | 인증키 또는 서버 접근 정보 포함 가능 |
| `key/`, `testkey/`     | 제외               | 민감정보 포함 가능                   |
| `.env`                 | 제외               | 실제 환경변수 포함 가능              |
| `.idea/`               | 제외               | 개인 IDE 설정                        |
| `__pycache__/`         | 제외               | Python cache                         |
| `.DS_Store`            | 제외               | OS cache                             |
| 대용량 모델 파일       | 검토 후 결정       | GitHub 용량 및 재현성 문제           |
| 외부 API key 포함 파일 | 제외 또는 sample화 | 보안 위험                            |

---

## 현재까지 완료된 매핑 요약

| 영역                               | 상태                 |
| ---------------------------------- | -------------------- |
| Backend API prototype              | 1차 반영 완료        |
| Database loader 및 SQL test schema | 반영 완료            |
| Recommendation architecture        | 문서화 완료          |
| Color extraction code              | 분리 완료            |
| Leaflet image selector code        | 분리 완료            |
| Image matching code                | 원본 보존, 분리 예정 |
| Exhibition recommendation code     | 원본 보존, 분리 예정 |
| AR 자료                            | 정리 예정            |
| Interior recommendation experiment | 검토 예정            |
| Business / IR 자료                 | 정리 예정            |
| Demo assets                        | 정리 예정            |
| Final README                       | 정리 예정            |

---

## 후속 작업 방향

이 매핑 문서를 기준으로 다음 작업을 진행한다.

1. Image matching 코드를 `tools/image-matching/`으로 분리한다.
2. Backend API를 routes/services/schemas 구조로 정리한다.
3. Leaflet service와 exhibition service를 backend 기능 모듈로 정리한다.
4. AR prototype 자료를 별도 폴더로 정리한다.
5. Interior recommendation experiment 자료를 검토 후 반영한다.
6. Business / IR / demo 자료를 문서화한다.
7. 최종 README에서 전체 기능을 연결한다.
