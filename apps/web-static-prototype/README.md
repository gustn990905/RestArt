# Web Static Prototype

이 폴더는 RestArt의 정적 웹 화면 prototype을 정리한 공간이다.

원본 화면 폴더에는 HTML, CSS, JavaScript, 이미지, 폰트, IDE 설정 파일이 함께 포함되어 있었지만, 이 repository에서는 화면 구조를 확인할 수 있는 HTML source만 선별하여 정리한다.

## 구성

```text
apps/web-static-prototype/
├─ README.md
└─ screens/
   ├─ artist_signup/
   ├─ exhibition/
   ├─ exhibition_detail/
   ├─ gallery/
   ├─ login/
   ├─ login_complete/
   ├─ main/
   ├─ mypage/
   ├─ nav/
   └─ user_signup/
```

## 포함 화면

| 화면                | 설명                      |
| ------------------- | ------------------------- |
| `main`              | RestArt 메인 화면         |
| `login`             | 로그인 화면               |
| `login_complete`    | 로그인 완료 화면          |
| `user_signup`       | 일반 사용자 회원가입 화면 |
| `artist_signup`     | 작가 회원가입 화면        |
| `mypage`            | 사용자 마이페이지 화면    |
| `gallery`           | 작품/갤러리 화면          |
| `exhibition`        | 전시 목록 화면            |
| `exhibition_detail` | 전시 상세 화면            |
| `nav`               | 공통 navigation 화면      |

## 정리 기준

이 폴더에는 HTML 화면 source만 포함한다.

다음 항목은 제외한다.

- 이미지 asset
- 작품 이미지
- 폰트 파일
- 외부 CSS library
- 외부 JavaScript library
- IDE 설정 파일
- 실행 결과물
- 임시 파일

## 기존 FastAPI prototype과의 관계

`apps/fastapi-web-prototype`은 FastAPI, Jinja2 template, image upload endpoint를 포함한 서버 기반 prototype이다.

`apps/web-static-prototype`은 별도의 정적 웹 화면 source를 정리한 공간이다.
두 prototype은 모두 RestArt 웹 서비스의 화면 구성을 보여주지만, 정리 기준과 원본 구조가 다르기 때문에 별도 폴더로 분리한다.

## 실행 참고

이 폴더에는 CSS, JavaScript, image asset을 포함하지 않기 때문에 단독 실행 시 화면 style이 완전히 재현되지 않을 수 있다.

정확한 화면 재현이 필요한 경우 원본 static asset을 별도 환경에 배치해야 한다.
