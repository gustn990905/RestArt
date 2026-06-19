# Planning Closeout

## 1. 문서 목적

이 문서는 RestArt 프로젝트의 초기 기획 정리 단계가 완료되었음을 기록한다.

1단계부터 3단계까지는 프로젝트 구조, 개요, 기획, 요구사항, MVP 범위, 개발 범위를 정리했다. 이후 단계에서는 백엔드, DB, AI, Unity/AR, 웹, 모바일, 디자인, 검증 자료를 실제 개발 산출물 중심으로 정리한다.

---

## 2. 1단계 산출물

1단계에서는 저장소 기본 구조를 생성했다.

### 산출물

- GitHub repository
- 기본 폴더 구조
- `.gitignore`
- `.gitkeep`

### 커밋

- `chore: initialize project directory structure`

### 의미

1단계은 RestArt 프로젝트 산출물을 체계적으로 정리하기 위한 저장소 기반을 마련한 단계이다.

---

## 3. 2단계 산출물

2단계에서는 프로젝트 개요와 초기 기획 문서를 작성했다.

### `docs/00-overview/`

- `project-overview.md`
- `problem-definition.md`
- `service-objective.md`
- `business-plan-summary.md`

### `docs/01-planning/`

- `core-feature-summary.md`
- `service-flow.md`
- `user-scenario.md`
- `business-model.md`

### 커밋

- `docs: add project overview documents`
- `docs: add initial planning documents`

### 의미

2단계는 RestArt가 어떤 서비스인지, 어떤 문제를 해결하려는지, 어떤 기능과 비즈니스 구조를 갖는지 정리한 단계이다.

---

## 4. 3단계 산출물

3단계에서는 기획 내용을 개발 가능한 요구사항으로 전환했다.

### `docs/02-requirements/`

- `product-requirements.md`
- `functional-requirements.md`
- `mvp-scope.md`
- `development-scope.md`
- `feature-priority.md`
- `non-functional-requirements.md`
- `roadmap.md`
- `planning-closeout.md`

### 커밋

- `docs: add product requirements`
- `docs: add functional requirements`
- `docs: define MVP scope`
- `docs: define development scope`
- `docs: add feature priority and non-functional requirements`
- `docs: close planning phase with roadmap`

### 의미

3단계는 기획을 마무리하고, 이후 실제 개발 산출물 정리로 넘어가기 위한 기준을 만든 단계이다.

---

## 5. 기획 마감 기준

RestArt의 초기 기획은 다음 기준을 충족했으므로 마감한다.

### 5.1 문제 정의 완료

다음 문제가 정리되었다.

- 장애·신진 예술인의 작품 노출 부족
- 사용자의 작품 구매 진입장벽
- 온라인 작품 구매의 불확실성
- 전시 경험의 일회성
- 소규모 전시의 디지털 홍보 한계

### 5.2 서비스 목표 완료

다음 목표가 정리되었다.

- AI 기반 작품 추천
- AR 작품 설치 시뮬레이션
- 작품 거래 및 리세일
- 개인화 모바일 리플릿
- 전시 홍보 및 SNS 공유
- 예술인과 사용자 간 선순환 구조

### 5.3 핵심 기능 정의 완료

다음 기능이 정리되었다.

- 사용자 기능
- 작가 기능
- 작품 등록
- 작품 DB
- 색상 추출
- 감성 분석
- 작품 추천
- AR 설치
- 거래/리세일
- 리플릿 생성
- 전시 추천

### 5.4 MVP 범위 정의 완료

MVP와 확장 기능을 구분했다.

- MVP: 작품 DB, 이미지 업로드, 색상 추출, 감성 태그, 작품 추천, 웹 기본 화면
- Phase 1: AR 설치, 작가 페이지, 컬렉션
- Phase 2: 리세일, 모바일 리플릿, 전시 추천
- Long-term: B2B/B2G 렌탈, PB 상품, 글로벌 서비스

### 5.5 개발 범위 정의 완료

다음 개발 산출물 범위를 정리했다.

- Backend/API
- Database
- AI Recommendation Model
- Unity/AR Placement Prototype
- Web Frontend
- Mobile Application
- Design Assets
- Validation and Demo Materials

---

## 6. 이후 개발 전환 기준

4단계부터는 기획 문서가 아니라 실제 개발 산출물 중심으로 진행한다.

전환 순서는 다음과 같다.

1. 백엔드/API 구조
2. 백엔드 API 프로토타입
3. DB 스키마
4. AI 추천 알고리즘 문서
5. AI 추천 모델 코드
6. Unity/AR 구현 문서
7. Unity/AR 프로젝트
8. 웹 프론트엔드
9. 웹 주요 기능
10. 모바일 앱
11. 디자인 자료
12. 검증 자료
13. 최종 README

---

## 7. 추가 기획 문서 처리 기준

이후 새 기획 자료가 있더라도 별도의 대규모 기획 문서로 추가하지 않는다.

대신 다음 방식으로 처리한다.

- 기능과 관련 있으면 해당 기능 문서에 반영
- 기술과 관련 있으면 `docs/06-architecture/`에 반영
- 화면과 관련 있으면 `docs/03-design/` 또는 `design/`에 반영
- 운영과 관련 있으면 16단계 release/roadmap 문서에 반영
- 최종 소개가 필요하면 README에 반영

---

## 8. 정리

RestArt의 초기 기획 문서는 3단계에서 마감한다.

이후 저장소는 기획 중심이 아니라 실제 개발 산출물 중심으로 정리한다. 4단계부터는 백엔드, DB, AI, Unity/AR, 웹, 모바일, 디자인, 검증 자료 순서로 진행한다.


