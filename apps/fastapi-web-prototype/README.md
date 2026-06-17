# FastAPI Web Prototype

이 폴더는 RestArt의 FastAPI 기반 웹 prototype 코드를 정리한 공간이다.

이 prototype은 Jinja2 template, static asset, 이미지 업로드 endpoint, K-means 기반 이미지 색상 clustering 기능, 추천 화면 route를 포함한다.

## 폴더 구조

```text
apps/fastapi-web-prototype/
├─ main.py
├─ templates/
├─ static/
└─ README.md
```

## 주요 기능

이 prototype은 다음 기능을 포함한다.

- FastAPI application 구성
- Jinja2 template 기반 화면 rendering
- static file serving
- 이미지 업로드 처리
- 업로드 이미지 저장
- K-means 기반 이미지 색상 clustering
- clustering 결과 이미지 저장
- 메인 화면 route
- 추천 화면 route

## 주요 source

```text
main.py
```

`main.py`는 FastAPI application의 진입점이다.

주요 역할은 다음과 같다.

| 구분              | 설명                             |
| ----------------- | -------------------------------- |
| `FastAPI`         | 웹 application 생성              |
| `StaticFiles`     | static asset 제공                |
| `Jinja2Templates` | HTML template rendering          |
| `/upload/`        | 이미지 업로드 및 clustering 처리 |
| `/`               | main page rendering              |
| `/ai_recomm`      | 추천 화면 rendering              |

## Route 구조

| Method | Path         | 역할                                  |
| ------ | ------------ | ------------------------------------- |
| `GET`  | `/`          | 메인 페이지 rendering                 |
| `GET`  | `/ai_recomm` | 추천 화면 rendering                   |
| `POST` | `/upload/`   | 이미지 업로드 및 clustering 결과 생성 |

## 이미지 업로드 처리

`/upload/` endpoint는 사용자가 업로드한 이미지 파일을 받아 다음 순서로 처리한다.

1. 업로드 폴더 생성
2. 결과 폴더 생성
3. 업로드 이미지 저장
4. K-means clustering 수행
5. clustering 결과 이미지 저장
6. 결과 이미지 경로 반환

업로드된 이미지는 다음 위치에 저장된다.

```text
static/uploads/
```

clustering 결과 이미지는 다음 위치에 저장된다.

```text
static/results/
```

## 이미지 색상 clustering

이미지 색상 clustering은 `save_clustered_image()` 함수에서 수행된다.

처리 흐름은 다음과 같다.

1. 이미지 열기
2. RGB 변환
3. numpy array 변환
4. pixel data reshape
5. K-means clustering 수행
6. cluster 중심값으로 이미지 재구성
7. 결과 이미지 저장

이 기능은 RestArt의 색상 기반 추천 구조와 연결된다.

## 추천 화면

`/ai_recomm` route는 추천 화면을 rendering한다.

현재 prototype에서는 감성 label 중 일부를 무작위로 선택하여 template에 전달한다.

이 구조는 이후 작품 감성 태그, 색상 분석 결과, 이미지 분석 결과와 결합하여 추천 결과를 구성하는 방식으로 확장될 수 있다.

## Template 구조

`templates/` 폴더에는 웹 화면 rendering에 사용되는 HTML template이 포함된다.

주요 template 예시는 다음과 같다.

```text
main_page.html
ai_recomm.html
artist_detail.html
artist_signup.html
exhibition.html
exhibition_detail.html
gallery.html
login.html
mypage.html
user_signup.html
```

## Static asset 구조

`static/` 폴더에는 화면별 CSS, JavaScript, 이미지 asset이 포함된다.

원본 개발 환경에서 생성된 IDE 설정, 가상환경, cache, private key, 임시 폴더는 제외하고 정리한다.

## 실행 방법

필요 package 설치 후 다음 명령으로 실행할 수 있다.

```bash
uvicorn main:app --reload
```

또는 `main.py`를 직접 실행할 수 있다.

```bash
python main.py
```

기본 실행 port는 `8000`이다.

## 필요 package

이 prototype은 다음 package를 사용한다.

```text
fastapi
uvicorn
jinja2
python-multipart
pillow
numpy
scikit-learn
```

## 제외 항목

이 폴더에는 다음 항목을 포함하지 않는다.

- 가상환경 폴더
- IDE 설정 폴더
- private key
- pem 파일
- cache 파일
- 임시 upload 결과
- 민감한 접속 정보
- 내부 설정 파일

## 정리 기준

이 폴더는 RestArt 웹 prototype의 화면 구조와 FastAPI 기반 이미지 처리 흐름을 보여주기 위한 코드만 포함한다.

원본 개발 환경의 불필요한 설정 파일과 민감정보는 제거하고, 실행 가능한 핵심 코드와 화면 template 중심으로 정리한다.
