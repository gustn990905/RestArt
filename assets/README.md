# RestArt Assets

이 폴더는 RestArt 프로젝트에서 사용하는 정적 자산의 관리 기준을 정리하기 위한 공간이다.

현재 repository에는 대용량 이미지, 영상, mockup 원본 자료를 포함하지 않는다. 실제 화면 확인과 기능 설명은 `apps/`, `docs/`, `tools/`, `experiments/`의 source와 문서를 기준으로 관리한다.

## Asset Management Policy

`assets/`에는 외부 공개가 가능하고 repository 관리에 적합한 최소 자산만 포함한다.

다음 항목은 포함하지 않는다.

- 대용량 이미지 결과물
- 영상 파일
- 임시 mockup 이미지
- 원본 발표자료
- 원본 사업 문서
- 개인 정보가 포함된 자료
- 외부 공개가 어려운 자료
- 자동 생성 결과물
- 임시 실행 결과물

## Current Structure

```text id="e7a6gy"
assets/
└─ README.md
```

현재 `assets/`에는 별도의 이미지, mockup, video 하위 폴더를 유지하지 않는다.

필요한 경우에만 목적이 명확한 하위 폴더를 새로 생성한다.

## When to Add Assets

다음 조건을 만족할 때만 `assets/`에 파일을 추가한다.

1. 프로젝트 설명에 반드시 필요한 자료일 것
2. 외부 공개가 가능한 자료일 것
3. 파일 크기가 repository 관리에 적합할 것
4. 파일명과 사용 목적이 명확할 것
5. source code나 문서와 연결되는 자료일 것

## Suggested Future Structure

추후 정적 자산이 필요한 경우 다음과 같이 목적별로 분리할 수 있다.

```text id="qfe8x0"
assets/
├─ images/
├─ mockups/
└─ videos/
```

| Folder     | Use Case                                  |
| ---------- | ----------------------------------------- |
| `images/`  | README나 문서 설명에 필요한 경량 이미지   |
| `mockups/` | 공개 가능한 화면 mockup                   |
| `videos/`  | 짧은 demo 영상 또는 외부 링크 설명용 자료 |

현재는 실제 자산을 포함하지 않으므로 위 폴더를 생성하지 않는다.

## Related Folders

| Area                 | Folder                                  |
| -------------------- | --------------------------------------- |
| 화면 prototype       | `apps/homepage-final-prototype/`        |
| 정적 web screen      | `apps/web-static-prototype/`            |
| FastAPI web template | `apps/fastapi-web-prototype/templates/` |
| 문서 목차            | `docs/README.md`                        |
| 디자인 기준          | `design/README.md`                      |

## Notes

대용량 이미지나 영상 자료는 repository에 직접 포함하기보다, 별도 저장소나 외부 링크로 관리하는 것이 적합하다.

GitHub repository에는 프로젝트 구조, code, 문서, 기능 설명에 필요한 최소 자료만 유지한다.
