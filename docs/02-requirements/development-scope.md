# Development Scope

## 1. 문서 목적

이 문서는 RestArt 프로젝트의 실제 개발 범위를 정리한다.

RestArt는 단순 기획 문서 프로젝트가 아니라, 웹, 모바일 앱, 백엔드/API, DB, AI 추천 알고리즘, Unity/AR 시뮬레이션, 디자인 산출물, 검증 자료를 포함하는 개발 프로젝트이다.

본 문서는 이후 4단계부터 진행할 개발 산출물 정리의 기준으로 사용한다.

---

## 2. 전체 개발 구성

RestArt의 개발 범위는 다음과 같이 구성된다.

1. Backend/API
2. Database
3. AI Recommendation Model
4. Unity/AR Placement Prototype
5. Web Frontend
6. Mobile Application
7. Design Assets
8. Validation and Demo Materials

---

## 3. Backend/API

### 목적

백엔드는 웹, 모바일 앱, 추천 모델, DB를 연결하는 중간 계층이다.

### 담당 기능

- 사용자 데이터 관리
- 작가 데이터 관리
- 작품 데이터 관리
- 이미지 업로드 요청 처리
- 색상 추출 요청 처리
- 작품 추천 요청 처리
- 추천 결과 반환
- 전시 리플릿 생성 요청 처리
- 전시 정보 조회
- 작품 거래 및 컬렉션 데이터 관리

### 정리 위치

- `apps/backend/`
- `apps/backend/api-prototype/`
- `docs/04-api/`

### 개발 산출물

- API prototype
- API scope 문서
- API endpoint 문서
- 환경변수 예시 파일
- 백엔드 README

---

## 4. Database

### 목적

DB는 작품, 작가, 사용자, 추천 결과, 거래, 리플릿, 전시 데이터를 저장한다.

### 주요 데이터

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

### 정리 위치

- `docs/05-database/`
- `apps/backend/database/`

### 개발 산출물

- ERD
- 테이블 정의서
- 데이터 딕셔너리
- schema.sql
- seed.example.sql
- 추천 데이터 흐름 문서

---

## 5. AI Recommendation Model

### 목적

AI 추천 모델은 사용자의 공간 이미지와 작품 DB를 비교하여 어울리는 작품을 추천한다.

### 담당 기능

- 이미지 대표 색상 추출
- RGB 값 및 색상 비율 계산
- 색상 테이블 매핑
- 감성 태그 매핑
- 감성 일치도 계산
- 켄달타우 기반 유사도 계산
- 추천 작품 정렬
- 개인화 리플릿용 작품 선정

### 정리 위치

- `tools/recommendation-model/`
- `docs/06-architecture/`

### 개발 산출물

- 색상 추출 코드
- 감성 매핑 코드
- 추천 알고리즘 코드
- 리플릿 생성 보조 코드
- 추천 파이프라인 문서
- 알고리즘 README

---

## 6. Unity/AR Placement Prototype

### 목적

Unity/AR 파트는 추천 작품을 사용자의 실제 공간에 가상으로 배치하는 기능을 제공한다.

### 담당 기능

- 작품 이미지 또는 오브젝트 배치
- 마커 또는 공간 인식 기반 배치
- 작품 크기와 위치 확인
- AR 시연 씬 구성
- 모바일 AR 시뮬레이션 연동

### 정리 위치

- `apps/unity-ar/`
- `docs/06-architecture/`
- `assets/demo/`

### 개발 산출물

- Unity 프로젝트
- AR placement scene
- 작품 배치 스크립트
- AR 시연 이미지 또는 영상
- Unity/AR 구현 문서

---

## 7. Web Frontend

### 목적

웹 프론트는 사용자가 공간 이미지를 업로드하고, 추천 결과와 작품 정보를 확인할 수 있는 화면을 제공한다.

### 담당 기능

- 메인 페이지
- 공간 이미지 업로드 화면
- 추천 결과 화면
- 작품 목록 화면
- 작품 상세 화면
- 작가 페이지
- 컬렉션 페이지
- 리플릿 화면
- 작품 거래 화면

### 정리 위치

- `apps/web/`
- `docs/03-design/`
- `docs/06-architecture/`

### 개발 산출물

- 웹 소스코드
- 컴포넌트 구조
- 기능별 페이지
- 웹 README
- 프론트엔드 아키텍처 문서

---

## 8. Mobile Application

### 목적

모바일 앱은 AR 설치 시뮬레이션, 전시장에서의 작품 촬영, 개인화 리플릿 생성 기능을 제공한다.

### 담당 기능

- 모바일 홈 화면
- 작품 추천 화면
- AR 작품 설치 화면
- 작품 촬영 기능
- 리플릿 생성 화면
- SNS 공유 기능
- 컬렉션 관리

### 정리 위치

- `apps/mobile/`
- `docs/06-architecture/`
- `design/screen-captures/mobile/`

### 개발 산출물

- 모바일 앱 소스코드
- 모바일 화면 컴포넌트
- AR 연동 화면
- 모바일 README
- 모바일/AR 연동 문서

---

## 9. Design Assets

### 목적

디자인 자료는 웹, 모바일, AR, 리플릿 화면의 사용자 경험을 설명한다.

### 정리 위치

- `design/figma/`
- `design/screen-captures/`
- `design/design-system/`
- `design/prototype-frames/`
- `assets/mockups/`

### 개발 산출물

- Figma 링크
- Figma 페이지 인덱스
- 웹 화면 캡처
- 모바일 화면 캡처
- AR 화면 캡처
- 디자인 시스템 문서
- 발표용 목업 이미지

---

## 10. Validation and Demo Materials

### 목적

검증 자료는 프로토타입과 기능 개발 결과를 보여주기 위해 정리한다.

### 정리 위치

- `docs/08-release/`
- `assets/demo/`
- `assets/videos/`

### 개발 산출물

- 사용자 테스트 요약
- A/B 테스트 요약
- 기능 시연 시나리오
- 데모 이미지 또는 영상
- 향후 개선 계획

---

## 11. 개발 산출물 정리 순서

4단계부터 개발 산출물은 다음 순서로 정리한다.

1. 백엔드/API 작업공간 및 범위
2. 백엔드 API 프로토타입
3. DB 스키마 및 데이터 구조
4. AI 추천 알고리즘 문서
5. AI 추천 모델 코드
6. Unity/AR 구현 문서
7. Unity/AR 프로젝트
8. 웹 프론트
9. 웹 주요 기능
10. 모바일 앱
11. 디자인 자료
12. 검증 및 릴리즈 자료
13. README

---

## 12. 정리

RestArt의 개발 범위는 기획 문서에 머무르지 않고 실제 서비스 구현에 필요한 주요 파트를 포함한다.

본 문서를 기준으로 이후 커밋은 백엔드, DB, AI, Unity/AR, 웹, 모바일, 디자인, 검증 순서로 진행한다.

