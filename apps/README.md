# RestArt Applications

이 폴더는 RestArt 프로젝트의 application prototype과 기능별 구현 자산을 정리한 공간이다.

RestArt는 공간 이미지 기반 작품 추천, 전시 추천, 모바일 리플릿 생성, backend API, web prototype을 포함하는 AI·AR 기반 아트테크 서비스이다. `apps/` 폴더는 실제 서비스 화면, backend prototype, API prototype, 정적 web prototype을 기능 단위로 구분해 관리한다.

## Application Structure

```text
apps/
├─ backend/
├─ backend-api-prototype/
├─ fastapi-web-prototype/
├─ homepage-final-prototype/
├─ mobile/
├─ web/
└─ web-static-prototype/
```

## Folder Overview

| Folder                      | Role                      | Description                                                                       |
| --------------------------- | ------------------------- | --------------------------------------------------------------------------------- |
| `backend/`                  | 기능별 backend 정리 공간  | API prototype, database, exhibition, leaflet 관련 backend 자산을 기능 단위로 정리 |
| `backend-api-prototype/`    | backend API prototype     | 작품, 전시, 이미지, 추천 기능을 API 형태로 실험한 Python backend prototype        |
| `fastapi-web-prototype/`    | FastAPI web prototype     | FastAPI 기반 web 화면과 추천 기능 연동 prototype                                  |
| `homepage-final-prototype/` | homepage screen prototype | 최종 homepage 화면에 가까운 HTML/CSS prototype                                    |
| `mobile/`                   | mobile app placeholder    | 모바일 리플릿 및 향후 mobile app 구현을 위한 구조 공간                            |
| `web/`                      | web app placeholder       | 향후 web application 구현을 위한 구조 공간                                        |
| `web-static-prototype/`     | static web prototype      | 주요 화면을 HTML 단위로 분리한 정적 web screen prototype                          |

## backend

```text
apps/backend/
├─ api-prototype/
├─ database/
├─ exhibition/
└─ leaflet/
```

`backend/` 폴더는 RestArt backend 기능을 주제별로 정리하기 위한 공간이다.

| Folder           | Description                           |
| ---------------- | ------------------------------------- |
| `api-prototype/` | API 기능 prototype 정리               |
| `database/`      | database 관련 구조와 연동 자산 정리   |
| `exhibition/`    | 전시 추천 및 전시 정보 처리 기능 정리 |
| `leaflet/`       | 모바일 리플릿 생성 기능 정리          |

## backend-api-prototype

```text
apps/backend-api-prototype/
├─ src/
├─ README.md
└─ requirements.txt
```

`backend-api-prototype/`은 RestArt의 backend API 기능을 Python 기반으로 정리한 prototype이다.

주요 기능은 다음과 같다.

- 전시 정보 API prototype
- 이미지 처리 API prototype
- 작품 추천 API prototype
- 대표 색상 및 이미지 유사도 처리
- database 연동 구조 정리
- backend module 분리 구조 확인

실행 및 세부 설명은 다음 문서를 기준으로 확인한다.

```text
apps/backend-api-prototype/README.md
```

## fastapi-web-prototype

```text
apps/fastapi-web-prototype/
├─ static/
├─ templates/
├─ main.py
└─ README.md
```

`fastapi-web-prototype/`은 FastAPI를 기반으로 web 화면과 추천 기능을 연결한 prototype이다.

주요 기능은 다음과 같다.

- FastAPI 기반 web routing
- Jinja template 기반 화면 구성
- 이미지 업로드 및 분석 흐름
- 색상 clustering 기반 추천 흐름
- 전시·작품·사용자 화면 prototype

실행 및 세부 설명은 다음 문서를 기준으로 확인한다.

```text
apps/fastapi-web-prototype/README.md
```

## homepage-final-prototype

`homepage-final-prototype/`은 RestArt homepage 화면을 HTML/CSS 중심으로 정리한 prototype이다.

포함된 주요 화면은 다음과 같다.

| File                   | Description         |
| ---------------------- | ------------------- |
| `main_final.html`      | main homepage 화면  |
| `artist_inform.html`   | 작가 정보 화면      |
| `exhibition.html`      | 전시 화면           |
| `filter2.html`         | 작품 filtering 화면 |
| `login2.html`          | login 화면          |
| `my_page.html`         | my page 화면        |
| `picture_sample2.html` | 작품 sample 화면    |
| `gpt.html`             | 실험 화면           |

관련 CSS 파일은 같은 폴더에 함께 정리되어 있다.

이 폴더는 정적 화면 prototype 성격이 강하며, backend 실행 파일이나 server entrypoint를 포함하지 않는다.

## web-static-prototype

```text
apps/web-static-prototype/
├─ screens/
└─ README.md
```

`web-static-prototype/`은 주요 화면을 기능별 screen 폴더로 나누어 정리한 정적 web prototype이다.

주요 화면 범위는 다음과 같다.

- 회원가입 화면
- login 화면
- main 화면
- nav 화면
- gallery 화면
- exhibition 화면
- exhibition detail 화면
- mypage 화면

세부 화면 목록은 다음 문서를 기준으로 확인한다.

```text
apps/web-static-prototype/README.md
```

## mobile

```text
apps/mobile/
└─ .gitkeep
```

`mobile/` 폴더는 모바일 리플릿 기능과 향후 mobile application 구현을 위한 구조 공간이다.

현재 핵심 설명은 다음 문서에서 관리한다.

```text
docs/12-mobile-leaflet/mobile-leaflet-flow.md
docs/12-mobile-leaflet/leaflet-result-structure.md
```

## web

```text
apps/web/
└─ .gitkeep
```

`web/` 폴더는 향후 main web application 구현을 위한 구조 공간이다.

현재 화면 prototype은 다음 폴더에서 확인한다.

```text
apps/homepage-final-prototype/
apps/web-static-prototype/
apps/fastapi-web-prototype/
```

## Related Documents

| Area                        | Document                                                 |
| --------------------------- | -------------------------------------------------------- |
| Project overview            | `docs/00-overview/project-overview.md`                   |
| Core features               | `docs/01-planning/core-feature-summary.md`               |
| Backend API scope           | `docs/04-api/backend-api-scope.md`                       |
| Backend module structure    | `docs/11-backend-api/backend-api-module-structure.md`    |
| Database overview           | `docs/05-database/database-overview.md`                  |
| Recommendation architecture | `docs/06-architecture/ai-recommendation-architecture.md` |
| Mobile leaflet flow         | `docs/12-mobile-leaflet/mobile-leaflet-flow.md`          |
| Exhibition recommendation   | `docs/13-exhibition/exhibition-recommendation-flow.md`   |

## Repository Policy

`apps/`에는 실행 또는 화면 확인에 필요한 source와 prototype만 포함한다.

다음 항목은 포함하지 않는다.

- 개인 정보가 포함된 원본 파일
- 실제 database 접속값
- 비공개 key 파일
- 환경설정 파일
- 대용량 이미지 결과물
- 자동 생성 cache
- 가상환경 폴더
- IDE 설정 폴더
- 임시 실행 결과물

## Suggested Review Order

RestArt application 구조를 확인할 때는 다음 순서로 보는 것이 좋다.

1. `apps/homepage-final-prototype/`
2. `apps/web-static-prototype/`
3. `apps/fastapi-web-prototype/README.md`
4. `apps/backend-api-prototype/README.md`
5. `apps/backend/`
6. `docs/README.md`
