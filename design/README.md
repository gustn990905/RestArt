# RestArt Design

이 폴더는 RestArt 프로젝트의 디자인 기준과 화면 구성 기준을 정리하기 위한 공간이다.

현재 repository에는 실제 디자인 원본 파일이나 화면 이미지 자료를 포함하지 않고, 서비스 화면 prototype과 HTML/CSS 구현 결과를 중심으로 관리한다.

## Design Structure

```text
design/
└─ design-system/
```

## Folder Overview

| Folder           | Role                  | Description                                                                              |
| ---------------- | --------------------- | ---------------------------------------------------------------------------------------- |
| `design-system/` | 디자인 기준 정리 공간 | 색상, typography, component guideline 등 향후 디자인 기준 문서를 정리하기 위한 구조 공간 |

## Current Design Sources

현재 실제 화면 prototype은 `design/`이 아니라 `apps/` 하위 폴더에서 관리한다.

| Folder                                  | Description                                         |
| --------------------------------------- | --------------------------------------------------- |
| `apps/homepage-final-prototype/`        | 최종 homepage 화면에 가까운 HTML/CSS prototype      |
| `apps/web-static-prototype/`            | 주요 화면을 screen 단위로 분리한 정적 web prototype |
| `apps/fastapi-web-prototype/templates/` | FastAPI web prototype에서 사용하는 template 화면    |

## Design Management Policy

`design/`에는 외부 공개 가능한 디자인 기준 문서만 포함한다.

다음 항목은 포함하지 않는다.

- 원본 디자인 작업 파일
- 개인 정보가 포함된 화면 자료
- 대용량 이미지 결과물
- 임시 화면 캡처
- 외부 공개가 어려운 발표자료
- 비공개 기획 원본 파일
- 자동 생성 파일

## Related Application Folders

| Area                  | Folder                                  |
| --------------------- | --------------------------------------- |
| Homepage prototype    | `apps/homepage-final-prototype/`        |
| Static web screens    | `apps/web-static-prototype/`            |
| FastAPI web templates | `apps/fastapi-web-prototype/templates/` |

## Related Documents

| Area              | Document                                   |
| ----------------- | ------------------------------------------ |
| Service overview  | `docs/00-overview/project-overview.md`     |
| Core features     | `docs/01-planning/core-feature-summary.md` |
| Service flow      | `docs/01-planning/service-flow.md`         |
| Application index | `apps/README.md`                           |

## Notes

현재 `design-system/`은 향후 디자인 기준 문서를 추가하기 위한 구조 공간이다.

추후 정리할 수 있는 항목은 다음과 같다.

- main color 기준
- button style 기준
- card component 기준
- typography 기준
- layout grid 기준
- mobile leaflet visual guideline
- artwork card visual guideline
