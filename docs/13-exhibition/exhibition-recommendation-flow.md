# 전시 추천 흐름

이 문서는 RestArt backend prototype의 전시 추천 기능 흐름을 정리한다.

전시 추천 기능은 사용자의 위치 정보를 기준으로 가까운 전시를 탐색하거나, 모바일 리플릿 생성 결과와 연결되는 추천 전시 정보를 제공하는 기능이다.

## 기능 목적

RestArt의 전시 추천 기능은 작품 추천 결과를 실제 전시 관람 경험으로 확장하기 위한 기능이다.

사용자는 공간 기반 작품 추천 또는 모바일 리플릿 생성 결과를 통해 작품 정보를 확인할 수 있고, 전시 추천 기능은 이 결과를 실제 전시 정보와 연결한다.

즉, 전시 추천 기능은 다음 흐름을 만든다.

1. 사용자가 작품 또는 공간 기반 추천 결과를 확인한다.
2. 시스템이 관련 전시 정보를 연결한다.
3. 사용자는 추천 작품과 연결된 전시를 탐색할 수 있다.
4. 작품 추천이 실제 전시 관람 경험으로 이어진다.

## 관련 endpoint

전시 추천 기능과 직접 연결되는 endpoint는 다음과 같다.

- GET /find_near_exhibition/
- POST /leaflet_creating/

## 관련 source

- apps/backend/api-prototype/main.py
- apps/backend/api-prototype/exhibition.py
- apps/backend/api-prototype/services/exhibition_service.py
- apps/backend/api-prototype/routes/exhibition_routes.py
- apps/backend/api-prototype/schemas/exhibition_schema.py
- tools/recommendation-model/prototype/image_utils.py

## 관련 함수

전시 추천 기능과 연결되는 주요 함수는 다음과 같다.

- find_nearby_exhibitions()
- find1_nearby_exhibitions()
- random_exhibition()

## 전시 추천 기능 구분

RestArt의 전시 추천 기능은 크게 두 가지 흐름으로 구분된다.

| 구분                       | 설명                                                    | 관련 endpoint              | 관련 함수                                             |
| -------------------------- | ------------------------------------------------------- | -------------------------- | ----------------------------------------------------- |
| 위치 기반 근처 전시 추천   | 사용자의 현재 위치를 기준으로 가까운 전시를 탐색한다.   | GET /find_near_exhibition/ | find_nearby_exhibitions(), find1_nearby_exhibitions() |
| 리플릿 결과 연결 전시 추천 | 모바일 리플릿 생성 결과 안에 추천 전시 정보를 포함한다. | POST /leaflet_creating/    | random_exhibition()                                   |

## 1. 위치 기반 근처 전시 추천 흐름

위치 기반 근처 전시 추천은 사용자의 위도와 경도 정보를 기준으로 주변 전시를 탐색하는 기능이다.

관련 endpoint는 다음과 같다.

GET /find_near_exhibition/

이 endpoint는 사용자의 위치 정보를 입력받고, 전시 데이터의 위치 정보와 비교하여 가까운 전시를 찾는다.

### 처리 흐름

1. 사용자의 위도와 경도 입력
2. 전시 데이터 조회
3. 전시명, 위도, 경도 정보 구성
4. 사용자 위치와 전시 위치 비교
5. 설정된 반경 기준으로 가까운 전시 탐색
6. 가장 적합한 전시명 선택
7. 선택된 전시의 상세 정보 조회
8. 전시 추천 결과 반환

### 입력 정보

위치 기반 전시 추천에서 사용하는 주요 입력 정보는 다음과 같다.

- 사용자 위도
- 사용자 경도
- 전시 위치 데이터
- 전시명
- 검색 반경

### 출력 정보

위치 기반 전시 추천 결과는 전시 상세 정보 형태로 반환된다.

반환 정보는 전시 데이터 구조에 따라 달라질 수 있으나, 일반적으로 다음 정보를 포함할 수 있다.

- 전시명
- 전시 위치
- 전시 상세 정보
- 전시 설명
- 전시 관련 이미지 또는 URL 정보

## 2. 리플릿 결과 연결 전시 추천 흐름

리플릿 결과 연결 전시 추천은 모바일 리플릿 생성 과정에서 추천 전시 정보를 함께 포함하는 흐름이다.

관련 endpoint는 다음과 같다.

POST /leaflet_creating/

이 흐름은 사용자가 입력한 작품 또는 전시 이미지에서 리플릿 결과를 생성할 때, 관련 전시 정보를 함께 연결하기 위해 사용된다.

### 처리 흐름

1. 사용자가 전시장 또는 작품 이미지를 입력한다.
2. 시스템이 입력 이미지와 작품 후보 이미지를 매칭한다.
3. 대표 이미지와 대표 색상 정보를 추출한다.
4. 색상 및 감성 기반 추천 작품을 선정한다.
5. 전시 후보 데이터를 조회한다.
6. 추천 전시 정보를 선택한다.
7. 리플릿 결과 안에 추천 전시 정보를 포함한다.

### recom_exhibition

리플릿 결과에서 추천 전시 정보는 `recom_exhibition` 항목과 연결된다.

이 값은 리플릿 생성 결과가 단순히 작품 추천에 머무르지 않고, 전시 정보와 함께 제공될 수 있도록 한다.

## 전시 추천과 다른 기능의 연결

전시 추천 기능은 RestArt의 다른 기능들과 연결된다.

### 모바일 리플릿 생성 기능과의 연결

모바일 리플릿 생성 기능은 작품 이미지 매칭, 대표 색상 추출, 작품 추천 결과를 생성한다.

전시 추천 기능은 이 결과에 추천 전시 정보를 연결하여, 사용자가 전시 맥락 안에서 작품 추천 결과를 이해할 수 있도록 한다.

### 공간 기반 작품 추천 기능과의 연결

공간 기반 작품 추천 기능은 사용자의 공간 이미지에 어울리는 작품을 추천한다.

전시 추천 기능은 이러한 작품 추천 결과가 실제 전시 탐색으로 확장될 수 있는 구조를 만든다.

### 이미지 매칭 기능과의 연결

전시 추천 자체는 위치 기반 탐색과 전시 정보 연결을 담당하지만, 모바일 리플릿 흐름에서는 이미지 매칭 결과와 함께 사용된다.

따라서 전시 추천은 이미지 매칭, 작품 추천, 리플릿 생성 결과와 함께 하나의 서비스 흐름을 구성한다.

## 구현 범위

현재 repository에서는 기존 backend prototype에 구현된 전시 추천 흐름을 기능 단위로 문서화한다.

기존 실행 흐름은 `apps/backend/api-prototype/main.py`에 보존되어 있으며, `services`, `routes`, `schemas` 폴더를 통해 전시 추천 기능을 분리 가능한 구조로 정리한다.

전시 데이터의 전체 원본, 내부 DB 값, 비공개 자료는 포함하지 않는다.

## 관련 문서

- apps/backend/exhibition/README.md
- docs/13-exhibition/nearby-exhibition-logic.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/12-mobile-leaflet/leaflet-result-structure.md
- docs/18-space-recommendation/space-artwork-recommendation-flow.md
- docs/05-database/database-overview.md
