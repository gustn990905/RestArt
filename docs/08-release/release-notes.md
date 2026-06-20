# RestArt 릴리즈 노트

이 문서는 RestArt 저장소의 정리 이력과 현재 공개 가능 상태를 요약한 릴리즈 노트이다.

현재 저장소는 production 배포본이 아니라, RestArt 프로젝트의 기획 문서, 개발 prototype, 추천 도구, 실험 자료를 정리한 개발 산출물 저장소이다.

## 1. 현재 릴리즈 성격

| 항목        | 내용                                                                     |
| ----------- | ------------------------------------------------------------------------ |
| 릴리즈 구분 | 저장소 정리 릴리즈                                                       |
| 목적        | 프로젝트 구조, 문서, prototype, 실험 자료를 외부 검토 가능한 형태로 정리 |
| 배포 성격   | production 배포 아님                                                     |
| 주요 대상   | 프로젝트 검토자, 개발자, 협업자                                          |
| 주요 범위   | 문서, backend prototype, web prototype, 추천 도구, 이미지·색상 분석 실험 |

## 2. 주요 정리 내용

이번 정리에서 다음 항목을 중심으로 저장소를 구성하였다.

| 영역                | 정리 내용                                      |
| ------------------- | ---------------------------------------------- |
| 루트 문서           | 프로젝트 전체 개요를 설명하는 `README.md` 작성 |
| 문서 목차           | `docs/README.md` 작성                          |
| 애플리케이션 구조   | `apps/README.md` 작성                          |
| 분석 도구 구조      | `tools/README.md` 작성                         |
| 실험 자료 구조      | `experiments/README.md` 작성                   |
| 디자인 관리 기준    | `design/README.md` 작성                        |
| 정적 자산 관리 기준 | `assets/README.md` 작성                        |
| 검증 기준           | `docs/08-release/validation-checklist.md` 작성 |

## 3. 저장소 구조 정리

현재 루트 구조는 다음과 같다.

```text
RestArt/
├─ apps/
├─ assets/
├─ design/
├─ docs/
├─ experiments/
├─ tools/
├─ .gitignore
└─ README.md
```

각 폴더의 역할은 다음과 같다.

| 폴더           | 역할                                                 |
| -------------- | ---------------------------------------------------- |
| `apps/`        | backend, web, homepage, static screen prototype 정리 |
| `assets/`      | 정적 자산 관리 기준 정리                             |
| `design/`      | 디자인 기준 문서 관리 공간                           |
| `docs/`        | 기획, 요구사항, DB, API, 아키텍처, 릴리즈 문서 정리  |
| `experiments/` | 색상 clustering, 멀티모달 감성 추출 실험 정리        |
| `tools/`       | 이미지 매칭, 추천 모델, 색상 분석 도구 정리          |

## 4. 삭제된 빈 placeholder 구조

실제 자료가 없는 빈 구조 폴더는 삭제하였다.

| 삭제 항목                  | 사유                                       |
| -------------------------- | ------------------------------------------ |
| `infra/`                   | 현재 배포 설정 파일을 포함하지 않음        |
| `packages/`                | 현재 공통 package 구조를 사용하지 않음     |
| `references/`              | 공개 가능한 참고 원본 자료를 포함하지 않음 |
| `assets/images/`           | 공개 이미지 자산을 포함하지 않음           |
| `assets/mockups/`          | 공개 mockup 자산을 포함하지 않음           |
| `assets/videos/`           | 공개 영상 자산을 포함하지 않음             |
| `design/figma/`            | 공개 디자인 원본 파일을 포함하지 않음      |
| `design/prototype-frames/` | 공개 prototype frame을 포함하지 않음       |
| `design/screen-captures/`  | 공개 화면 캡처 자료를 포함하지 않음        |

## 5. 문서 정리 내용

`docs/` 폴더에는 다음 문서 영역이 정리되어 있다.

| 영역                       | 내용                                                              |
| -------------------------- | ----------------------------------------------------------------- |
| `00-overview/`             | 프로젝트 개요, 문제 정의, 서비스 목표, 사업 요약                  |
| `01-planning/`             | 비즈니스 모델, 핵심 기능, 서비스 흐름, 사용자 시나리오            |
| `02-requirements/`         | 제품 요구사항, 기능 요구사항, 비기능 요구사항, 개발 범위          |
| `04-api/`                  | backend API 범위                                                  |
| `05-database/`             | DB 개요, table 정의, 데이터 사전, 추천 데이터 흐름                |
| `06-architecture/`         | 추천 구조, 색상 추출, 감성 매핑, 유사도 ranking, 리플릿 추천 구조 |
| `08-release/`              | 검증 체크리스트와 릴리즈 노트                                     |
| `09-source-inventory/`     | 원본 source 대응 및 기능 coverage 정리                            |
| `10-image-matching/`       | 이미지 매칭 흐름                                                  |
| `11-backend-api/`          | backend API module 구조                                           |
| `12-mobile-leaflet/`       | 모바일 리플릿 흐름과 결과 구조                                    |
| `13-exhibition/`           | 전시 추천 흐름과 근처 전시 탐색 logic                             |
| `14-ai-experiments/`       | 색상 분석, 감성 추출, 추천 알고리즘 실험                          |
| `18-space-recommendation/` | 공간 기반 작품 추천 흐름                                          |

## 6. 애플리케이션 prototype 정리

`apps/` 폴더에는 다음 prototype이 정리되어 있다.

| 영역                        | 내용                                                |
| --------------------------- | --------------------------------------------------- |
| `backend-api-prototype/`    | Python 기반 backend API prototype                   |
| `fastapi-web-prototype/`    | FastAPI 기반 web prototype                          |
| `homepage-final-prototype/` | HTML/CSS 기반 homepage prototype                    |
| `web-static-prototype/`     | 화면 단위 static web prototype                      |
| `backend/`                  | API, DB, exhibition, leaflet 관련 backend 정리 공간 |

## 7. 분석 도구와 실험 자료 정리

`tools/`와 `experiments/`에는 추천 기능과 이미지 분석 기능의 기반 자료가 정리되어 있다.

| 영역                                         | 내용                                                     |
| -------------------------------------------- | -------------------------------------------------------- |
| `tools/image_matching/`                      | 이미지 로딩, 전처리, feature matching, similarity 계산   |
| `tools/recommendation-model/`                | 색상 사전, 색상 추출, 유사도 계산, 리플릿 생성 관련 도구 |
| `experiments/color-clustering-prototypes/`   | 이미지 대표 색상 추출과 clustering 실험                  |
| `experiments/multimodal-emotion-extraction/` | 작품 이미지와 설명 기반 감성 추출 실험                   |

## 8. 검증 상태

현재 저장소는 다음 기준으로 검증하였다.

| 항목                                | 상태  |
| ----------------------------------- | ----- |
| 주요 폴더별 README 존재 여부        | 확인  |
| 불필요한 빈 placeholder 폴더 삭제   | 완료  |
| 실제 DB 접속값 하드코딩 여부        | 없음  |
| 실제 서비스 인증 정보 포함 여부     | 없음  |
| 개인 자료 포함 여부                 | 없음  |
| 대용량 비공개 이미지·영상 포함 여부 | 없음  |
| 작업 트리 상태                      | clean |
| 원격 저장소 반영                    | 완료  |

## 9. 실행 관련 제한 사항

현재 저장소는 개발 산출물과 prototype을 정리한 상태이다.

실제 실행을 위해서는 다음 항목이 추가로 필요하다.

- 로컬 실행 환경 구성
- Python package 설치
- DB 설정
- 테스트 데이터 구성
- API 실행 절차 보완
- FastAPI 실행 절차 보완
- 실행 검증 기록 작성

현재 로컬 Python launcher가 정상 동작하지 않는 상태이므로, Python 문법 검사와 backend 실행 검증은 보류 상태로 정리한다.

## 10. 다음 보완 가능 항목

향후 저장소 품질을 높이기 위해 다음 항목을 추가할 수 있다.

| 항목            | 설명                                       |
| --------------- | ------------------------------------------ |
| 실행 가이드     | backend와 FastAPI prototype 실행 절차 정리 |
| dependency 정리 | Python package version 고정                |
| sample data     | 공개 가능한 테스트용 sample data 구성      |
| API 사용 예시   | 주요 endpoint 요청·응답 예시 정리          |
| 화면 흐름 문서  | web prototype 화면 이동 흐름 정리          |
| 검증 결과 문서  | 실행 테스트 결과와 한계 정리               |
| release tag     | 안정 정리본에 version tag 부여             |

## 11. 릴리즈 요약

현재 RestArt 저장소는 다음 상태로 정리되어 있다.

- 프로젝트 개요 문서 정리 완료
- 기능별 문서 목차 정리 완료
- backend 및 web prototype 정리 완료
- 추천 모델과 이미지 분석 도구 정리 완료
- 색상·감성 분석 실험 자료 정리 완료
- 공개에 부적합한 원본 자료 제외
- 불필요한 빈 폴더 제거
- 실제 민감값 노출 없음
- 원격 저장소 반영 완료

현재 릴리즈는 RestArt 프로젝트를 설명하고 검토하기 위한 공개 가능한 개발 산출물 정리본이다.
