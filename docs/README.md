# RestArt Documentation

이 폴더는 RestArt 프로젝트의 기획, 요구사항, API, DB, 아키텍처, 추천 알고리즘, 이미지 분석, 전시 추천, 모바일 리플릿 관련 문서를 기능별로 정리한 공간이다.

루트 `README.md`가 프로젝트 전체 소개를 담당한다면, 이 문서는 `docs/` 내부 문서의 목차와 탐색 기준을 제공한다.

## Documentation Structure

```text
docs/
├─ 00-overview/
├─ 01-planning/
├─ 02-requirements/
├─ 03-design/
├─ 04-api/
├─ 05-database/
├─ 06-architecture/
├─ 07-meeting/
├─ 08-release/
├─ 09-source-inventory/
├─ 10-image-matching/
├─ 11-backend-api/
├─ 12-mobile-leaflet/
├─ 13-exhibition/
├─ 14-ai-experiments/
└─ 18-space-recommendation/
```

## 00-overview

프로젝트의 기본 개요와 문제 정의를 정리한다.

| Document                   | Description                      |
| -------------------------- | -------------------------------- |
| `project-overview.md`      | RestArt 프로젝트 개요            |
| `problem-definition.md`    | 예술인과 사용자 사이의 문제 정의 |
| `service-objective.md`     | 서비스 목표와 확장 방향          |
| `business-plan-summary.md` | 사업계획 요약                    |

## 01-planning

서비스 기획과 사용자 흐름을 정리한다.

| Document                  | Description     |
| ------------------------- | --------------- |
| `business-model.md`       | 비즈니스 모델   |
| `core-feature-summary.md` | 핵심 기능 요약  |
| `service-flow.md`         | 서비스 흐름     |
| `user-scenario.md`        | 사용자 시나리오 |

## 02-requirements

개발 범위와 요구사항을 정리한다.

| Document                         | Description     |
| -------------------------------- | --------------- |
| `product-requirements.md`        | 제품 요구사항   |
| `functional-requirements.md`     | 기능 요구사항   |
| `non-functional-requirements.md` | 비기능 요구사항 |
| `mvp-scope.md`                   | MVP 범위        |
| `feature-priority.md`            | 기능 우선순위   |
| `development-scope.md`           | 개발 범위       |
| `roadmap.md`                     | 개발 로드맵     |
| `planning-closeout.md`           | 기획 정리 문서  |

## 03-design

디자인과 화면 설계 관련 문서를 정리하는 공간이다.

현재는 구조 공간을 유지하며, 화면 설계나 디자인 시스템 문서를 추가할 수 있다.

## 04-api

API 범위와 backend 기능 구조를 정리한다.

| Document               | Description      |
| ---------------------- | ---------------- |
| `backend-api-scope.md` | backend API 범위 |

## 05-database

작품, 전시, 추천 기능에 필요한 데이터 구조를 정리한다.

| Document                      | Description      |
| ----------------------------- | ---------------- |
| `database-overview.md`        | DB 전체 개요     |
| `table-definition.md`         | table 정의       |
| `data-dictionary.md`          | 데이터 사전      |
| `recommendation-data-flow.md` | 추천 데이터 흐름 |

## 06-architecture

추천 알고리즘과 분석 pipeline 구조를 정리한다.

| Document                                 | Description          |
| ---------------------------------------- | -------------------- |
| `ai-recommendation-architecture.md`      | 추천 구조            |
| `color-extraction-pipeline.md`           | 색상 추출 pipeline   |
| `emotion-mapping-pipeline.md`            | 감성 매핑 pipeline   |
| `similarity-ranking-logic.md`            | 유사도 ranking logic |
| `leaflet-recommendation-architecture.md` | 리플릿 추천 구조     |

## 07-meeting

회의록이나 진행 기록을 정리하는 공간이다.

현재는 폴더 구조를 유지한다.

## 08-release

배포, release note, 버전 정리 문서를 위한 공간이다.

현재는 폴더 구조를 유지한다.

## 09-source-inventory

원본 자료와 정리된 source의 대응 관계를 정리한다.

| Document                  | Description      |
| ------------------------- | ---------------- |
| `source-inventory.md`     | source 목록      |
| `original-file-map.md`    | 원본 파일 대응표 |
| `feature-coverage-map.md` | 기능별 정리 범위 |

## 10-image-matching

이미지 매칭 기능의 흐름과 기준을 정리한다.

| Document                 | Description           |
| ------------------------ | --------------------- |
| `image-matching-flow.md` | 이미지 매칭 처리 흐름 |

## 11-backend-api

backend API 모듈 구조를 정리한다.

| Document                          | Description           |
| --------------------------------- | --------------------- |
| `backend-api-module-structure.md` | backend API 모듈 구성 |

## 12-mobile-leaflet

모바일 리플릿 생성 기능을 정리한다.

| Document                      | Description             |
| ----------------------------- | ----------------------- |
| `mobile-leaflet-flow.md`      | 모바일 리플릿 생성 흐름 |
| `leaflet-result-structure.md` | 리플릿 결과 구조        |

## 13-exhibition

전시 추천 기능을 정리한다.

| Document                            | Description          |
| ----------------------------------- | -------------------- |
| `exhibition-recommendation-flow.md` | 전시 추천 흐름       |
| `nearby-exhibition-logic.md`        | 근처 전시 탐색 logic |

## 14-ai-experiments

색상 분석, 감성 추출, 멀티모달 분석 실험을 정리한다.

| Document                              | Description             |
| ------------------------------------- | ----------------------- |
| `color-analysis-summary.md`           | 색상 분석 요약          |
| `emotion-and-color-table-summary.md`  | 감성·색상 table 요약    |
| `multimodal-emotion-extraction.md`    | 멀티모달 감성 추출 실험 |
| `recommendation-algorithm-summary.md` | 추천 알고리즘 요약      |

## 18-space-recommendation

공간 기반 작품 추천 기능을 정리한다.

| Document                               | Description                     |
| -------------------------------------- | ------------------------------- |
| `space-artwork-recommendation-flow.md` | 공간 이미지 기반 작품 추천 흐름 |

## 정리 기준

`docs/`에는 프로젝트 이해와 기능 설명에 필요한 문서만 포함한다.

다음 항목은 직접 포함하지 않는다.

- 개인정보가 포함된 원본 문서
- 계약서, 통장 사본, 서명 이미지
- 원본 사업계획서 전체 파일
- 대용량 이미지 결과물
- 실행 결과물
- 임시 파일
- 비공개 설정값

## 문서 탐색 순서

처음 프로젝트를 확인하는 경우 다음 순서로 보면 된다.

1. `00-overview/project-overview.md`
2. `00-overview/problem-definition.md`
3. `01-planning/core-feature-summary.md`
4. `02-requirements/product-requirements.md`
5. `06-architecture/ai-recommendation-architecture.md`
6. `05-database/database-overview.md`
7. `11-backend-api/backend-api-module-structure.md`
8. `12-mobile-leaflet/mobile-leaflet-flow.md`
9. `13-exhibition/exhibition-recommendation-flow.md`
10. `14-ai-experiments/recommendation-algorithm-summary.md`
