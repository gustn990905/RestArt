# Homepage Final Prototype

이 폴더는 RestArt 홈페이지 최종 화면 prototype에서 HTML/CSS source만 선별해 정리한 공간이다.

원본 화면 폴더에는 이미지, 작품 이미지, 로고, 홍보 이미지, IDE 설정 파일이 함께 포함되어 있었지만, 이 repository에서는 화면 구조와 스타일 구현을 확인할 수 있는 HTML/CSS 파일만 포함한다.

## 구성

apps/homepage-final-prototype/

- README.md
- artist_inform.html
- artist_inform.css
- exhibition.html
- exhibition.css
- filter2.html
- filter2.css
- gpt.html
- indexstyle.css
- login2.html
- main_final.html
- main_final.css
- my_page.html
- mypage.css
- nav_top3.css
- picture_sample2.html
- picture.css

## 포함 화면

| File                   | 설명                          |
| ---------------------- | ----------------------------- |
| `main_final.html`      | RestArt 메인 홈페이지 화면    |
| `artist_inform.html`   | 작가 정보 화면                |
| `exhibition.html`      | 전시 화면                     |
| `filter2.html`         | 필터 기반 화면                |
| `login2.html`          | 로그인 화면                   |
| `my_page.html`         | 마이페이지 화면               |
| `picture_sample2.html` | 작품 소개 또는 작품 샘플 화면 |
| `gpt.html`             | 실험용 화면 prototype         |

## 포함 스타일

| File                | 설명                   |
| ------------------- | ---------------------- |
| `main_final.css`    | 메인 화면 스타일       |
| `artist_inform.css` | 작가 정보 화면 스타일  |
| `exhibition.css`    | 전시 화면 스타일       |
| `filter2.css`       | 필터 화면 스타일       |
| `mypage.css`        | 마이페이지 스타일      |
| `picture.css`       | 작품 화면 스타일       |
| `indexstyle.css`    | index 계열 화면 스타일 |
| `nav_top3.css`      | navigation 스타일      |

## 정리 기준

이 폴더에는 HTML/CSS source만 포함한다.

다음 항목은 제외한다.

- 이미지 asset
- 작품 이미지
- 로고 이미지
- 홍보 이미지
- IDE 설정 파일
- 압축 파일
- 문서 파일
- 발표자료
- 임시 파일

## 기존 web prototype과의 관계

`apps/web-static-prototype`은 RestArt 웹 화면의 정적 HTML prototype을 정리한 공간이다.

`apps/homepage-final-prototype`은 별도 폴더에 있던 홈페이지 최종 화면 source를 HTML/CSS 중심으로 정리한 공간이다.

두 폴더는 모두 RestArt 웹 화면 구현을 보여주지만, 원본 위치와 화면 구성 차이가 있어 별도로 분리한다.

## 참고 사항

이 폴더에는 이미지와 외부 asset을 포함하지 않기 때문에 단독 실행 시 화면이 완전히 재현되지 않을 수 있다.

정확한 화면 재현이 필요한 경우 원본 이미지와 정적 asset을 별도 실행 환경에 배치해야 한다.
