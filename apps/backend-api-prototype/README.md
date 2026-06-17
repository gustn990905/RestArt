# Backend API Prototype

이 폴더는 RestArt의 backend API prototype 코드를 정리한 공간이다.

FastAPI 기반 endpoint, 이미지 분석 유틸리티, 작품 이미지 추천 로직, 전시 정보 처리, MySQL 연동 script를 포함한다. DB 접속값은 코드에 직접 포함하지 않고, 환경변수 기반 설정으로 정리한다.

## 구성

```text
apps/backend-api-prototype/
├─ README.md
├─ requirements.txt
└─ src/
   ├─ main4.py
   ├─ exhibition.py
   ├─ images.py
   ├─ recommend_picture.py
   ├─ restartdb.py
   ├─ signiture_color.py
   ├─ spectral_image.py
   └─ mkapi/
      ├─ __init__.py
      └─ image_utils.py
```
