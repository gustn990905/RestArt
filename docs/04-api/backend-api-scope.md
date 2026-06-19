# Backend API Scope

## 개요

이 문서는 RestArt 프로젝트의 백엔드/API 개발 범위를 정의한다.

RestArt는 AI·AR 기반 아트테크 플랫폼으로, 사용자 공간 이미지 분석, 작품 추천, 작품 DB 저장, 전시 리플릿 생성, 전시 정보 조회, 작품 거래 기능이 백엔드와 연결된다.

백엔드는 웹, 모바일 앱, 추천 알고리즘, DB, AR 시뮬레이션 기능을 연결하는 중간 계층으로 동작한다.

---

## 백엔드 역할

RestArt 백엔드는 다음 역할을 담당한다.

1. 사용자 및 작가 데이터 관리
2. 작품 이미지와 작품 메타데이터 저장
3. 작품 색상 및 감성 분석 결과 저장
4. 사용자 공간 이미지 기반 추천 요청 처리
5. 추천 알고리즘 결과 반환
6. 전시 리플릿 생성 요청 처리
7. 전시 정보 및 추천 전시 데이터 제공
8. 작품 거래 및 컬렉션 데이터 관리

---

## 주요 기능 범위

### 1. Artwork API

작품 등록, 조회, 수정, 삭제를 담당한다.

작품 등록 시 저장되는 정보는 다음과 같다.

- 작품 ID
- 작가 ID
- 작가명 또는 닉네임
- 작품명
- 작품 이미지 URL
- 작품 설명
- 감성 태그
- 대표 색상
- 색상 비율
- 가격 정보
- 거래 상태

Artwork API는 추천 알고리즘과 작품 상세 페이지의 기반 데이터가 된다.

---

### 2. Artist API

작가 정보를 관리한다.

작가 페이지는 작품 노출과 판매 가능성을 높이기 위한 기능이다.

관리 대상 정보는 다음과 같다.

- 작가 ID
- 작가명
- 작가 소개
- 작가 프로필 이미지
- 등록 작품 목록
- 전시 또는 협업 정보

---

### 3. User API

사용자 계정과 컬렉션 데이터를 관리한다.

사용자는 작품 추천, 컬렉션 저장, 작품 구매, 리세일, 리플릿 생성 기능을 사용할 수 있다.

관리 대상 정보는 다음과 같다.

- 사용자 ID
- 닉네임
- 관심 작품
- 구매 작품
- 컬렉션
- 리플릿 생성 기록
- 추천 이력

---

### 4. Recommendation API

사용자 공간 이미지 또는 전시장에서 촬영한 작품 이미지를 기반으로 추천 결과를 생성한다.

추천 API의 입력값은 다음과 같다.

- 사용자 ID
- 공간 이미지
- 추출된 대표 색상
- 색상 비율
- 감성 태그
- 추천 요청 유형

추천 API의 출력값은 다음과 같다.

- 추천 작품 목록
- 추천 점수
- 감성 일치 정보
- 색상 유사도 정보
- 추천 사유

---

### 5. Image Analysis API

이미지 분석 API는 작품 이미지와 공간 이미지에서 색상 및 감성 정보를 추출한다.

주요 처리 내용은 다음과 같다.

- 이미지 업로드
- 이미지 전처리
- 대표 색상 추출
- 색상 비율 계산
- 감성 태그 생성
- 분석 결과 저장

---

### 6. Leaflet API

전시 경험 기반 개인화 모바일 리플릿을 생성한다.

사용자가 전시장에서 촬영한 작품 이미지를 기반으로 취향을 분석하고, 개인화된 리플릿을 생성한다.

리플릿 생성 결과에는 다음 정보가 포함된다.

- 전시 정보
- 사용자 대표 이미지
- 촬영 작품 목록
- 취향 분석 결과
- 추천 작품
- 추천 전시
- SNS 공유용 데이터

---

### 7. Exhibition API

전시 정보를 등록하고 조회한다.

전시 리플릿 기능과 추천 전시 기능을 위해 사용된다.

관리 대상 정보는 다음과 같다.

- 전시 ID
- 전시명
- 전시 기관
- 전시 소개
- 전시 이미지 또는 포스터
- 전시 위치
- 전시 기간
- 관련 작품 목록

---

### 8. Transaction API

작품 구매, 거래, 리세일 데이터를 관리한다.

관리 대상 정보는 다음과 같다.

- 거래 ID
- 구매자 ID
- 판매자 또는 작가 ID
- 작품 ID
- 거래 상태
- 결제 상태
- 리세일 여부
- 거래 생성일

---

## 추천 데이터 처리 흐름

### 작품 등록 흐름

작가 작품 등록
→ 작품 이미지 업로드
→ 작품명 및 설명 입력
→ 이미지 색상 추출
→ 감성 분석
→ 작가 검수 및 수정
→ 작품 DB 저장

### 사용자 추천 흐름

사용자 공간 사진 업로드
→ 이미지 전처리
→ 대표 색상 추출
→ 색상 비율 계산
→ 감성 매핑
→ 작품 DB와 비교
→ 추천 작품 목록 생성
→ 추천 결과 저장
→ 웹 또는 모바일 앱으로 반환

### 전시 리플릿 흐름

전시장에서 작품 촬영
→ 촬영 이미지 저장
→ 대표 작품 선정
→ 취향 분석
→ 추천 작품 및 전시 생성
→ 모바일 리플릿 생성
→ SNS 공유 데이터 반환

---

## 실제 API 프로토타입 후보

기존 개발 산출물 기준으로 다음 API 흐름을 정리 대상으로 둔다.

### 1. 감성 기반 인테리어 추천 API

- 사용자 인테리어 이미지 입력
- 이미지 색상 분석
- 감성 또는 대표 색상 기반 작품 추천
- 추천 결과 반환

예상 endpoint:

- `POST /find_emotion_interior/`

### 2. 주변 전시 조회 API

- 사용자 위치 정보 입력
- 전시 DB와 거리 비교
- 가까운 전시 목록 반환

예상 endpoint:

- `GET /find_near_exhibition/`

### 3. 개인화 리플릿 생성 API

- 사용자가 촬영한 작품 이미지 목록 입력
- 대표 색상 및 취향 분석
- 추천 작품 및 추천 전시 생성
- 모바일 리플릿 결과 반환

예상 endpoint:

- `POST /leaflet_creating/`

### 4. 대표 색상 분석 API

- 이미지 입력
- 대표 RGB 값과 색상 비율 분석
- 추천 모델 또는 리플릿 생성에 활용

예상 endpoint:

- `POST /analyze-most-common-rgb/`

### 5. 대표 작품 선정 API

- 여러 작품 이미지 입력
- 색상 거리 또는 클러스터링 기반 대표 작품 선정
- 리플릿 구성에 활용

예상 endpoint:

- `POST /analyze-most-different-pictures/`

---

## 데이터 저장 범위

백엔드는 다음 데이터를 DB와 연결한다.

- 사용자 데이터
- 작가 데이터
- 작품 데이터
- 작품 색상 데이터
- 작품 감성 데이터
- 공간 이미지 분석 데이터
- 추천 결과 데이터
- 컬렉션 데이터
- 거래 데이터
- 전시 데이터
- 리플릿 데이터

---

## API 프로토타입 구조

초기 API 프로토타입은 다음 구조로 정리한다.

- `apps/backend/api-prototype/`
  - API 엔트리포인트
  - 이미지 분석 요청 처리
  - 추천 요청 처리
  - 전시 리플릿 요청 처리

- `apps/backend/database/`
  - DB schema
  - seed example
  - migration file
  - 작품 데이터 loader

- `tools/recommendation-model/prototype/`
  - 색상 추출 로직
  - 감성 매핑 로직
  - 추천 알고리즘
  - 리플릿 생성 보조 로직

---

## 보안 및 저장소 관리 기준

백엔드 코드 정리 시 다음 파일과 정보는 저장소에 포함하지 않는다.

- `.env`
- DB password
- AWS access key
- `.pem` 파일
- `key/`
- `testkey/`
- 실제 운영 DB host
- 실제 운영 계정명
- 실제 운영 데이터 dump
- IDE 설정 파일
- Python cache 파일

환경변수는 `.env.example` 형태로만 제공한다.

예상 환경변수는 다음과 같다.

- `DB_HOST`
- `DB_PORT`
- `DB_NAME`
- `DB_USER`
- `DB_PASSWORD`
- `AWS_ACCESS_KEY_ID`
- `AWS_SECRET_ACCESS_KEY`
- `S3_BUCKET_NAME`

---

## 향후 구현 구조

향후 백엔드 코드는 다음 구조로 정리한다.

- `apps/backend/app/main.py`
- `apps/backend/app/config.py`
- `apps/backend/app/database.py`
- `apps/backend/app/routers/recommendation.py`
- `apps/backend/app/routers/exhibition.py`
- `apps/backend/app/routers/leaflet.py`
- `apps/backend/app/routers/artwork.py`
- `apps/backend/app/routers/user.py`
- `apps/backend/app/routers/artist.py`
- `apps/backend/app/services/`
- `apps/backend/app/repositories/`
- `apps/backend/database/schema.sql`
- `apps/backend/database/seed.example.sql`

---

## 4단계 정리

4단계의 목적은 RestArt의 백엔드/API 개발 범위를 정의하고, 이후 실제 API 코드와 추천 알고리즘 코드를 정리할 수 있는 구조를 만드는 것이다.

다음 단계에서는 API 프로토타입 코드, 이미지 분석 유틸, 작품 DB loader를 프로젝트 구조에 맞게 정리한다.


