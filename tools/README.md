# RestArt Tools

이 폴더는 RestArt 프로젝트의 이미지 매칭, 색상 분석, 작품 추천, 리플릿 생성 관련 도구와 prototype module을 정리한 공간이다.

`tools/`는 application 실행 코드와 분리하여, 추천 로직이나 이미지 처리 로직처럼 독립적으로 재사용할 수 있는 기능 단위 code를 관리한다.

## Tools Structure

```text
tools/
├─ image_matching/
└─ recommendation-model/
```

## Folder Overview

| Folder                  | Role             | Description                                                                    |
| ----------------------- | ---------------- | ------------------------------------------------------------------------------ |
| `image_matching/`       | 이미지 매칭 도구 | 작품 이미지와 입력 이미지의 특징을 비교하고 유사도를 계산하는 module           |
| `recommendation-model/` | 추천 모델 도구   | 색상 사전, 색상 추출, 리플릿 생성, 유사도 계산, 추천 prototype을 정리한 module |

## image_matching

```text
tools/image_matching/
├─ feature_matcher.py
├─ image_loader.py
├─ image_preprocessing.py
├─ matching_service.py
├─ similarity.py
├─ __init__.py
└─ README.md
```

`image_matching/`은 이미지 기반 작품 매칭 기능을 구성하는 도구 모음이다.

주요 역할은 다음과 같다.

- 이미지 파일 로딩
- 이미지 전처리
- 특징점 또는 feature 추출
- 이미지 간 similarity 계산
- matching service 단위 기능 구성
- 작품 추천 또는 이미지 검색 기능과의 연동 가능성 검토

### Module Description

| File                     | Description                            |
| ------------------------ | -------------------------------------- |
| `image_loader.py`        | 이미지 입력 및 로딩 처리               |
| `image_preprocessing.py` | 이미지 전처리 처리                     |
| `feature_matcher.py`     | 이미지 feature matching 처리           |
| `similarity.py`          | 이미지 간 유사도 계산                  |
| `matching_service.py`    | 이미지 매칭 기능을 service 단위로 구성 |
| `__init__.py`            | Python package 인식용 파일             |
| `README.md`              | image matching module 설명             |

세부 내용은 다음 문서를 기준으로 확인한다.

```text
tools/image_matching/README.md
```

## recommendation-model

```text
tools/recommendation-model/
├─ color_dictionary/
├─ color_extraction/
├─ leaflet_generation/
├─ prototype/
├─ similarity/
└─ README.md
```

`recommendation-model/`은 RestArt의 작품 추천 기능을 구성하는 주요 분석 도구를 정리한 공간이다.

주요 역할은 다음과 같다.

- 입력 이미지의 대표 색상 추출
- 색상 사전 기반 색상명 변환
- 색상과 감성 정보의 연결
- 작품 데이터와 사용자 입력값의 similarity 계산
- exhibition leaflet 생성 기능의 추천 logic 검토
- 추천 알고리즘 prototype 관리

### Subfolder Description

| Folder                | Description                                 |
| --------------------- | ------------------------------------------- |
| `color_dictionary/`   | 색상명, 대표 색상, 색상 사전 관련 code      |
| `color_extraction/`   | 이미지에서 대표 색상을 추출하는 code        |
| `leaflet_generation/` | 전시 사진 기반 모바일 리플릿 생성 관련 code |
| `prototype/`          | 추천 기능 실험 prototype                    |
| `similarity/`         | 작품·색상·이미지 유사도 계산 logic          |

세부 내용은 다음 문서를 기준으로 확인한다.

```text
tools/recommendation-model/README.md
```

## Relationship with Applications

`tools/`는 직접 실행되는 service application이라기보다, `apps/`의 prototype이나 backend 기능에서 재사용할 수 있는 분석 module 성격을 가진다.

| Related Area                     | Connection                                     |
| -------------------------------- | ---------------------------------------------- |
| `apps/backend-api-prototype/`    | 추천 API, 이미지 처리 API와 연결 가능          |
| `apps/fastapi-web-prototype/`    | web upload, 이미지 분석, 추천 화면과 연결 가능 |
| `apps/homepage-final-prototype/` | 화면 prototype과 기능 연결 기준 제공           |
| `apps/web-static-prototype/`     | 정적 화면의 추천 기능 설명 기준 제공           |
| `docs/06-architecture/`          | 추천 구조와 pipeline 설명 문서와 연결          |
| `docs/10-image-matching/`        | 이미지 매칭 처리 흐름 문서와 연결              |
| `docs/14-ai-experiments/`        | 색상·감성 분석 실험 문서와 연결                |

## Related Documents

| Area                             | Document                                                            |
| -------------------------------- | ------------------------------------------------------------------- |
| Recommendation architecture      | `docs/06-architecture/ai-recommendation-architecture.md`            |
| Color extraction pipeline        | `docs/06-architecture/color-extraction-pipeline.md`                 |
| Emotion mapping pipeline         | `docs/06-architecture/emotion-mapping-pipeline.md`                  |
| Similarity ranking               | `docs/06-architecture/similarity-ranking-logic.md`                  |
| Image matching flow              | `docs/10-image-matching/image-matching-flow.md`                     |
| Color analysis summary           | `docs/14-ai-experiments/color-analysis-summary.md`                  |
| Recommendation algorithm summary | `docs/14-ai-experiments/recommendation-algorithm-summary.md`        |
| Space artwork recommendation     | `docs/18-space-recommendation/space-artwork-recommendation-flow.md` |

## Management Policy

`tools/`에는 기능 검토와 재사용에 필요한 source code만 포함한다.

다음 항목은 포함하지 않는다.

- 개인 정보가 포함된 파일
- 실제 database 접속값
- 외부 공개가 어려운 인증 정보
- 대용량 이미지 결과물
- 자동 생성 cache
- 가상환경 폴더
- IDE 설정 폴더
- 임시 실행 결과물
- 원본 기획서 전체 파일

## Suggested Review Order

RestArt의 분석 도구 구조를 확인할 때는 다음 순서로 보는 것이 좋다.

1. `tools/recommendation-model/README.md`
2. `tools/recommendation-model/color_dictionary/`
3. `tools/recommendation-model/color_extraction/`
4. `tools/recommendation-model/similarity/`
5. `tools/image_matching/README.md`
6. `docs/06-architecture/ai-recommendation-architecture.md`
7. `docs/10-image-matching/image-matching-flow.md`
