# Roadmap

## 1. 문서 목적

이 문서는 RestArt 저장소의 4단계 이후 개발 산출물 정리 순서를 정의한다.

1단계부터 3단계까지는 프로젝트 구조, 개요, 기획, 요구사항을 정리했다. 4단계부터는 실제 개발 산출물 중심으로 백엔드, DB, AI, Unity/AR, 웹, 모바일, 디자인, 검증 자료를 순차적으로 정리한다.

---

## 2. 진행 완료

### 1단계. Repository Setup

완료 내용은 다음과 같다.

- GitHub 저장소 생성
- 기본 폴더 구조 생성
- `.gitignore` 생성
- 초기 push

커밋 메시지:

- `chore: initialize project directory structure`

---

### 2단계. Project Overview and Initial Planning

완료 내용은 다음과 같다.

- 프로젝트 개요 문서
- 문제 정의 문서
- 서비스 목표 문서
- 사업계획 요약 문서
- 핵심 기능 요약 문서
- 서비스 흐름 문서
- 사용자 시나리오 문서
- 비즈니스 모델 문서

커밋 메시지:

- `docs: add project overview documents`
- `docs: add initial planning documents`

---

### 3단계. Product Requirements and Development Scope

완료 예정 내용은 다음과 같다.

- 제품 요구사항
- 기능 요구사항
- MVP 범위
- 개발 범위
- 기능 우선순위
- 비기능 요구사항
- 로드맵
- 기획 마감 문서

커밋 메시지:

- `docs: add product requirements`
- `docs: add functional requirements`
- `docs: define MVP scope`
- `docs: define development scope`
- `docs: add feature priority and non-functional requirements`
- `docs: close planning phase with roadmap`

---

## 3. 4단계 이후 개발 정리 계획

### 4단계. Backend/API Workspace and Scope

작업 내용:

- 백엔드/API 작업공간 생성
- 추천모델 작업공간 생성
- `.gitignore` 보강
- 백엔드 API 범위 문서 작성

예상 커밋 메시지:

- `chore: prepare backend and recommendation workspace`
- `docs: define backend API and data pipeline scope`

---

### 5단계. Backend API Prototype

작업 내용:

- API 프로토타입 코드 정리
- 환경변수 기반 설정 분리
- API 실행 README 작성
- 민감정보 제거

예상 커밋 메시지:

- `feat: add initial backend API prototype`

---

### 6단계. Database Schema and Data Structure

작업 내용:

- DB 스키마 문서 작성
- 테이블 정의서 작성
- 데이터 딕셔너리 작성
- schema.sql 또는 seed.example.sql 정리

예상 커밋 메시지:

- `docs: add database schema documents`
- `feat: add initial database schema`

---

### 7단계. AI Recommendation Architecture

작업 내용:

- 색상 추출 구조 문서
- 감성 매핑 구조 문서
- 추천 파이프라인 문서
- 리플릿 추천 로직 문서

예상 커밋 메시지:

- `docs: add AI recommendation architecture`

---

### 8단계. AI Recommendation Pipeline

작업 내용:

- 색상 추출 코드
- 감성 매핑 코드
- 켄달타우 추천 코드
- 리플릿 생성 보조 코드
- 추천 모델 README

예상 커밋 메시지:

- `feat: add artwork recommendation pipeline`

---

### 9단계. Unity/AR Implementation Notes

작업 내용:

- Unity/AR 구조 문서
- 작품 배치 흐름 문서
- AR 시연 구조 문서
- 3D/AR 파일 관리 기준 정리

예상 커밋 메시지:

- `docs: add Unity AR implementation notes`

---

### 10단계. Unity AR Placement Prototype

작업 내용:

- Unity 프로젝트 정리
- AR scene 정리
- 작품 배치 스크립트 정리
- 시연 파일 정리

예상 커밋 메시지:

- `feat: add Unity AR placement prototype`

---

### 11단계. Web Frontend

작업 내용:

- 웹 프로젝트 기본 코드 정리
- 기본 화면 구조 정리
- 웹 실행 README 작성

예상 커밋 메시지:

- `feat: add initial web application source`

---

### 12단계. Web Feature Pages

작업 내용:

- 작품 추천 페이지
- 작품 목록 페이지
- 작품 상세 페이지
- 작가 페이지
- 리플릿 페이지
- 마이페이지

예상 커밋 메시지:

- `feat: add artwork and leaflet web pages`

---

### 13단계. Mobile Application

작업 내용:

- 모바일 앱 코드 정리
- 모바일 화면 구조 정리
- 모바일 실행 README 작성

예상 커밋 메시지:

- `feat: add initial mobile application source`

---

### 14단계. Figma and Screen Captures

작업 내용:

- Figma 링크 정리
- Figma 페이지 인덱스 작성
- 웹 화면 캡처 정리
- 모바일 화면 캡처 정리
- Unity/AR 시연 화면 캡처 정리

예상 커밋 메시지:

- `design: add figma references and screen captures`

---

### 15단계. Design System and Mockups

작업 내용:

- 색상 문서
- 폰트 문서
- 컴포넌트 문서
- 레이아웃 규칙
- 발표용 목업 이미지

예상 커밋 메시지:

- `design: add design system and prototype mockups`

---

### 16단계. Validation and Release Roadmap

작업 내용:

- 사용자 테스트 요약
- A/B 테스트 요약
- 시연 시나리오
- 향후 개선 계획
- release note

예상 커밋 메시지:

- `docs: add validation summary and release roadmap`

---

### 17단계. Portfolio README

작업 내용:

- 최종 README 작성
- 프로젝트 소개
- 기술 스택
- 시스템 구조
- 핵심 기능
- 화면 이미지
- 실행 방법
- 개발 과정
- 향후 계획

예상 커밋 메시지:

- `docs: add portfolio README`

---

## 4. 정리

3단계 이후에는 기획 문서 추가를 최소화하고, 실제 개발 산출물 중심으로 정리한다.

기획 문서는 3단계에서 마감하며, 이후에는 개발 산출물 설명에 필요한 범위에서만 보완한다.


