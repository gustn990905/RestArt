# RestArt

RestArt는 사용자의 공간 이미지와 취향 데이터를 분석하여 어울리는 예술 작품을 추천하고, AR 시뮬레이션과 작품 거래 구조로 연결하는 AI·AR 기반 아트테크 플랫폼이다.

이 저장소는 RestArt 프로젝트의 기획 문서, 요구사항, 디자인 구조, 추천 알고리즘, 이미지 분석 실험, 웹 prototype, backend API prototype을 기능별로 정리한 저장소이다.

## Project Background

RestArt는 장애·신진 예술인의 작품이 충분히 발견되지 못하고, 사용자는 자신에게 맞는 작품을 고르기 어렵다는 문제에서 출발했다.

기존 온라인 미술 플랫폼은 작품 판매, 작가 정보 제공, 경매, 조각투자 중심으로 구성되는 경우가 많다. RestArt는 사용자의 공간 이미지와 감성 데이터를 기반으로 작품을 추천하고, AR을 통해 실제 공간에 작품을 배치했을 때의 느낌을 확인할 수 있도록 설계되었다.

## Core Concept

RestArt의 핵심은 작품을 단순히 나열하는 것이 아니라, 사용자의 공간과 취향을 기준으로 작품을 발견하게 만드는 것이다.

주요 구조는 다음과 같다.

- 공간 이미지 기반 색상 분석
- 색상·감성 기반 작품 추천
- 작품 상세 정보 및 작가 정보 제공
- AR 작품 설치 시뮬레이션
- 작품 거래 및 리세일 구조
- 전시 경험 기반 개인화 모바일 리플릿 생성
- SNS 공유와 커뮤니티 확장

## Key Features

| Feature                            | Description                                                                |
| ---------------------------------- | -------------------------------------------------------------------------- |
| Space-based artwork recommendation | 사용자의 공간 이미지에서 주요 색상을 추출하고, 공간에 어울리는 작품을 추천 |
| Emotion and color matching         | 색상과 감성 태그를 활용해 작품과 사용자 취향을 매칭                        |
| AR artwork simulation              | 추천 작품을 실제 공간에 가상 배치하여 구매 전 적합성 확인                  |
| Mobile leaflet generation          | 전시장에서 촬영한 작품 이미지를 바탕으로 개인화 모바일 리플릿 생성         |
| Exhibition recommendation          | 위치와 취향 정보를 활용한 전시 추천                                        |
| Image matching                     | 이미지 유사도, 색상 cluster, 감성 태그를 활용한 작품 매칭                  |
| Backend API prototype              | FastAPI 기반 추천, 색상 분석, 이미지 분석, 전시 추천 API 구조              |
| Web prototype                      | RestArt 웹 화면과 홈페이지 prototype 정리                                  |

## Repository Structure

```text
RestArt/
├─ apps/
│  ├─ backend/
│  ├─ backend-api-prototype/
│  ├─ fastapi-web-prototype/
│  ├─ homepage-final-prototype/
│  ├─ mobile/
│  ├─ web/
│  └─ web-static-prototype/
├─ assets/
├─ design/
├─ docs/
├─ experiments/
├─ infra/
├─ packages/
├─ references/
└─ tools/
```

## Main App Prototypes

| Path                             | Description                           |
| -------------------------------- | ------------------------------------- |
| `apps/fastapi-web-prototype/`    | FastAPI와 Jinja2 기반 웹 prototype    |
| `apps/web-static-prototype/`     | 정적 HTML 화면 prototype              |
| `apps/backend-api-prototype/`    | FastAPI 기반 backend API prototype    |
| `apps/homepage-final-prototype/` | 홈페이지 최종 화면 HTML/CSS prototype |
| `apps/backend/`                  | 기능별 backend 정리 문서와 prototype  |
| `apps/mobile/`                   | 모바일 관련 구조 정리 공간            |
| `apps/web/`                      | 웹 애플리케이션 구조 정리 공간        |

## Documentation

| Path                            | Description                                          |
| ------------------------------- | ---------------------------------------------------- |
| `docs/00-overview/`             | 프로젝트 개요, 문제 정의, 서비스 목표, 사업계획 요약 |
| `docs/01-planning/`             | 기획 문서                                            |
| `docs/02-requirements/`         | 요구사항 정리                                        |
| `docs/03-design/`               | 디자인 및 화면 설계                                  |
| `docs/04-api/`                  | API 문서                                             |
| `docs/05-database/`             | DB 구조 및 데이터 설명                               |
| `docs/06-architecture/`         | 서비스 아키텍처                                      |
| `docs/09-source-inventory/`     | 원본 파일 및 source 정리                             |
| `docs/10-image-matching/`       | 이미지 매칭 기능 문서                                |
| `docs/11-backend-api/`          | backend API 정리                                     |
| `docs/12-mobile-leaflet/`       | 모바일 리플릿 기능 정리                              |
| `docs/13-exhibition/`           | 전시 추천 기능 정리                                  |
| `docs/14-ai-experiments/`       | 색상·감성·멀티모달 분석 실험 정리                    |
| `docs/18-space-recommendation/` | 공간 기반 작품 추천 기능 정리                        |

## Experiments and Tools

| Path                                         | Description                          |
| -------------------------------------------- | ------------------------------------ |
| `experiments/color-clustering-prototypes/`   | 색상 clustering 실험 code            |
| `experiments/multimodal-emotion-extraction/` | 이미지 기반 감성 추출 실험           |
| `tools/image_matching/`                      | 이미지 매칭 관련 도구                |
| `tools/recommendation-model/`                | 추천 모델, 색상 사전, prototype code |

## Backend API Prototype

`apps/backend-api-prototype/`은 RestArt의 backend API prototype을 정리한 공간이다.

주요 기능은 다음과 같다.

- 이미지 URL 기반 작품 분석
- 색상 cluster 분석
- 대표 색상 추출
- 작품 이미지 매칭
- 근처 전시 추천
- 모바일 리플릿 생성 정보 반환
- MySQL 기반 작품·전시 데이터 조회 및 저장

DB 접속값은 코드에 직접 포함하지 않고, 환경변수 기반으로 정리한다.

```text
RESTART_DB_HOST
RESTART_DB_USER
RESTART_DB_PASSWORD
RESTART_DB_NAME
```

## Web Prototypes

RestArt의 웹 화면 prototype은 목적에 따라 분리되어 있다.

| Path                             | Role                                       |
| -------------------------------- | ------------------------------------------ |
| `apps/fastapi-web-prototype/`    | FastAPI server와 Jinja2 template 기반 화면 |
| `apps/web-static-prototype/`     | 원본 정적 HTML 화면 구조                   |
| `apps/homepage-final-prototype/` | 홈페이지 최종 화면 HTML/CSS source         |

이미지, 폰트, 외부 library bundle, IDE 설정 파일, 실행 결과물은 저장소에 직접 포함하지 않는다.

## Service Objective

RestArt의 목표는 예술인의 작품이 더 쉽게 발견되고, 사용자가 자신의 공간과 취향에 맞는 작품을 더 쉽게 선택할 수 있는 디지털 예술 소비 환경을 만드는 것이다.

이를 위해 RestArt는 AI 추천, AR 시뮬레이션, 작품 거래, 리플릿 생성, SNS 공유 기능을 결합한 아트테크 플랫폼을 지향한다.

## Target Users

| User                | Needs                                                       |
| ------------------- | ----------------------------------------------------------- |
| 일반 사용자         | 자신의 공간과 취향에 맞는 작품 추천, 구매 전 설치 느낌 확인 |
| 예술인              | 작품 노출 확대, 판매 기회 확보, 작가 브랜딩                 |
| 전시 및 기관 운영자 | 전시 홍보, 관람객 참여형 콘텐츠, 디지털 리플릿 제공         |

## Excluded from Repository

다음 항목은 저장소에 직접 포함하지 않는다.

- 실제 DB 접속값
- 비공개 key 파일
- 환경설정 파일
- 가상환경 폴더
- IDE 설정 폴더
- cache 파일
- 실행 결과물
- 원본 사업계획서·계약서·개인정보 포함 문서
- 대용량 이미지 결과물
- 통장 사본, 서명 이미지 등 민감 자료

## Status

현재 저장소는 RestArt의 기획, 문서, prototype code, 추천 알고리즘, 이미지 분석 실험을 기능별로 정리하는 단계이다.

주요 prototype과 문서는 순차적으로 정리되어 있으며, 실행 환경 재현보다 source 구조와 기능 흐름 설명에 초점을 둔다.
