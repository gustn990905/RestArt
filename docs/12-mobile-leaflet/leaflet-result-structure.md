# 모바일 리플릿 결과 구조

이 문서는 RestArt backend prototype의 모바일 리플릿 생성 기능에서 반환되는 결과 구조를 정리한다.

모바일 리플릿 결과는 사용자 이미지 분석 결과, 대표 색상 정보, 추천 작품, 관련 전시 정보, 리플릿 디자인 타입을 포함하는 형태로 구성된다.

## 관련 endpoint

POST /leaflet_creating/

## 관련 source

- apps/backend/api-prototype/main.py
- apps/backend/api-prototype/services/leaflet_service.py
- apps/backend/api-prototype/routes/leaflet_routes.py
- apps/backend/api-prototype/schemas/leaflet_schema.py
- tools/recommendation-model/leaflet_generation/leaflet_image_selector.py
- tools/image_matching/

## 결과 구조 개요

모바일 리플릿 생성 결과는 다음 정보를 중심으로 구성된다.

- user_color
- user_rgb
- recom_picture1
- recom_picture2
- spectral_key
- recom_exhibition
- leaflet_design

## user_color

`user_color`는 사용자 입력 이미지에서 추출된 대표 색상 또는 색상 그룹을 의미한다.

이 값은 리플릿의 시각적 방향성과 추천 작품 선정에 사용된다.

주요 역할은 다음과 같다.

- 사용자 이미지의 대표 색상 표현
- 색상 기반 작품 추천 기준
- 리플릿 디자인 타입 선택 기준
- 사용자 이미지와 작품 데이터 사이의 색상 연결 기준

## user_rgb

`user_rgb`는 사용자 이미지에서 추출된 대표 색상의 RGB 값을 의미한다.

이 값은 색상 분석 결과를 구체적인 수치 형태로 표현하기 위해 사용된다.

주요 역할은 다음과 같다.

- 대표 색상의 수치 표현
- 색상 비교 및 색상 그룹 판단 근거
- 리플릿 결과 화면에서 색상 시각화에 활용 가능
- 색상 기반 추천 로직과 디자인 선택 로직의 연결값

## recom_picture1

`recom_picture1`은 색상 기반 추천 작품 후보를 의미한다.

사용자 이미지에서 추출한 대표 색상과 작품 데이터의 색상 정보를 비교하여 선정되는 추천 결과다.

주요 역할은 다음과 같다.

- 색상 유사성 기반 작품 추천
- 사용자 이미지와 시각적으로 어울리는 작품 제안
- 대표 색상과 작품 색상 cluster 사이의 연결 결과
- 리플릿 결과에서 첫 번째 추천 작품 영역 구성

## recom_picture2

`recom_picture2`는 감성 또는 분위기 기반 추천 작품 후보를 의미한다.

색상 기준만으로 추천 결과를 구성하지 않고, 작품의 감성 정보까지 함께 고려하기 위한 결과다.

주요 역할은 다음과 같다.

- 감성 기반 작품 추천
- 사용자 이미지의 분위기와 연결되는 작품 제안
- 색상 추천 결과를 보완하는 추천 축
- 리플릿 결과에서 두 번째 추천 작품 영역 구성

## spectral_key

`spectral_key`는 색상 또는 이미지 분석 과정에서 도출되는 분류 기준값으로 사용된다.

기존 prototype에서는 색상 그룹, 이미지 분석 결과, 추천 기준을 연결하는 값으로 활용된다.

주요 역할은 다음과 같다.

- 색상 분석 결과와 추천 로직 연결
- 리플릿 디자인 선택의 기준값
- 추천 결과 분류 기준
- 이미지 분석 결과를 리플릿 구성 요소로 변환하는 중간 기준

## recom_exhibition

`recom_exhibition`은 리플릿 결과에 연결되는 추천 전시 정보를 의미한다.

모바일 리플릿 기능은 작품 추천 결과만 제공하는 것이 아니라, 관련 전시 정보와 연결될 수 있다.

주요 역할은 다음과 같다.

- 추천 전시 정보 제공
- 작품 추천 결과와 전시 관람 흐름 연결
- 리플릿 결과의 전시 맥락 강화
- 사용자가 작품 추천 이후 실제 전시 탐색으로 이어질 수 있도록 지원

## leaflet_design

`leaflet_design`은 최종 리플릿의 디자인 타입 또는 레이아웃 선택 결과를 의미한다.

대표 이미지, 대표 색상, 색상 그룹 분석 결과를 바탕으로 리플릿 디자인 방향을 결정한다.

주요 역할은 다음과 같다.

- 개인화 리플릿 디자인 타입 결정
- 색상 기반 시각 스타일 연결
- 모바일 리플릿 화면 구성 기준
- 사용자 이미지 분석 결과를 시각적 결과물로 변환

## 데이터 흐름 요약

모바일 리플릿 결과는 다음 흐름을 거쳐 구성된다.

1. 사용자 이미지 입력
2. 작품 후보 이미지와 매칭
3. 대표 이미지 선정
4. 대표 색상 추출
5. 색상 기반 작품 추천
6. 감성 기반 작품 추천
7. 관련 전시 정보 연결
8. 리플릿 디자인 타입 결정
9. 최종 리플릿 결과 반환

## 기능적 의미

모바일 리플릿 결과 구조는 단순히 추천 작품 목록만 반환하는 구조가 아니다.

사용자 이미지에서 도출된 색상, RGB, 감성, 추천 작품, 전시 정보, 디자인 타입을 하나의 결과로 묶어 전시 관람 경험을 개인화하는 구조다.

따라서 이 기능은 RestArt의 다음 기능들과 연결된다.

- 이미지 매칭
- 색상 분석
- 감성 기반 추천
- 작품 추천
- 전시 추천
- 모바일 리플릿 디자인 생성

## 구현 범위

현재 repository에서는 기존 backend prototype의 리플릿 생성 흐름을 보존하면서, 결과 구조를 문서화한다.

이 문서는 실제 응답 필드의 의미를 설명하기 위한 문서이며, 민감한 원본 데이터나 내부 DB 값은 포함하지 않는다.

또한 원본 사업 문서나 내부 기획 문서를 그대로 포함하지 않고, 공개 가능한 기능 구조와 기술 흐름만 정리한다.

## 관련 문서

- apps/backend/leaflet/README.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md
- docs/10-image-matching/image-matching-flow.md
- docs/06-architecture/leaflet-recommendation-logic.md
