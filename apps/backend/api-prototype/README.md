# Backend API Prototype

## 개요

이 폴더는 RestArt 백엔드 API 프로토타입 코드를 정리한 공간이다.

RestArt는 사용자 공간 이미지 분석, 작품 추천, 전시 리플릿 생성, 주변 전시 조회, 작품 DB 저장 기능을 포함하는 AI·AR 기반 아트테크 플랫폼이다.

이 백엔드 프로토타입은 웹, 모바일 앱, 추천 알고리즘, DB를 연결하는 API 계층의 초기 구현을 정리한다.

---

## 파일 구성

| 파일                   | 역할                                                                                       |
| ---------------------- | ------------------------------------------------------------------------------------------ |
| `main.py`              | FastAPI 메인 엔트리포인트. 인테리어 추천, 주변 전시 조회, 리플릿 생성 API 흐름을 포함한다. |
| `config.py`            | DB 접속 정보를 환경변수에서 읽어오는 공통 설정 파일이다.                                   |
| `.env.example`         | 실행에 필요한 환경변수 예시 파일이다. 실제 비밀번호는 포함하지 않는다.                     |
| `exhibition.py`        | 전시 정보 처리 및 전시 데이터 관련 보조 코드이다.                                          |
| `recommend_picture.py` | 사용자 이미지와 작품 이미지를 비교하여 추천 후보를 찾는 보조 코드이다.                     |
| `signature_color.py`   | 이미지에서 대표 RGB 색상과 색상명을 추출하는 색상 분석 API 후보이다.                       |
| `spectral_image.py`    | 여러 이미지 간 유사도 비교와 대표 이미지 선정을 위한 분석 코드이다.                        |
| `requirements.txt`     | Python 실행에 필요한 패키지 목록이다.                                                      |

---

## 주요 API 후보

### 1. 인테리어 이미지 기반 작품 추천

사용자의 공간 이미지를 분석하여 색상과 감성에 어울리는 작품을 추천한다.

예상 endpoint:

- `POST /find_emotion_interior/`

### 2. 주변 전시 조회

사용자의 위치 정보를 기반으로 가까운 전시 정보를 조회한다.

예상 endpoint:

- `GET /find_near_exhibition/`

### 3. 개인화 리플릿 생성

사용자가 전시장에서 촬영한 작품 이미지를 기반으로 개인화 모바일 리플릿을 생성한다.

예상 endpoint:

- `POST /leaflet_creating/`

### 4. 대표 색상 분석

이미지에서 가장 많이 나타나는 RGB 색상과 색상명을 분석한다.

예상 endpoint:

- `POST /analyze-most-common-rgb/`

### 5. 대표 이미지 선정

여러 작품 이미지 중 리플릿에 사용할 대표 이미지를 선정한다.

예상 endpoint:

- `POST /analyze-most-different-pictures/`

---

## 환경변수 설정

실제 DB 접속 정보는 코드에 직접 작성하지 않는다.

`.env.example` 파일을 참고하여 로컬에서 `.env` 파일을 생성한다.

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=restartdb
DB_USER=root
DB_PASSWORD=
DB_CHARSET=utf8mb4
```
