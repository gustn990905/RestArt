# 전시 추천 기능

이 문서는 RestArt backend prototype의 전시 추천 기능을 정리한다.

전시 추천 기능은 사용자 위치를 기준으로 가까운 전시를 찾거나, 모바일 리플릿 생성 결과와 연결되는 추천 전시 정보를 제공하는 기능이다.

## 기능 역할

RestArt의 전시 추천 기능은 작품 추천 결과를 실제 전시 관람 흐름과 연결하기 위한 기능이다.

사용자는 작품 또는 공간 기반 추천 결과를 확인한 뒤, 관련 전시 정보를 함께 확인할 수 있다. 이를 통해 RestArt는 단순 작품 추천 서비스가 아니라 작품, 전시, 관람 경험을 연결하는 서비스 구조를 가진다.

## 주요 기능 구분

전시 추천 기능은 크게 두 가지 흐름으로 구분된다.

| 구분                       | 설명                                               | 관련 endpoint              |
| -------------------------- | -------------------------------------------------- | -------------------------- |
| 위치 기반 근처 전시 추천   | 사용자의 위도와 경도를 기준으로 가까운 전시를 탐색 | GET /find_near_exhibition/ |
| 리플릿 결과 연결 전시 추천 | 모바일 리플릿 결과에 추천 전시 정보를 연결         | POST /leaflet_creating/    |

## 관련 backend source

- apps/backend/api-prototype/main.py
- apps/backend/api-prototype/exhibition.py
- apps/backend/api-prototype/services/exhibition_service.py
- apps/backend/api-prototype/routes/exhibition_routes.py
- apps/backend/api-prototype/schemas/exhibition_schema.py

## 관련 prototype utility source

- tools/recommendation-model/prototype/image_utils.py

## 관련 함수

전시 추천 기능과 직접 연결되는 함수는 다음과 같다.

- find_nearby_exhibitions()
- find1_nearby_exhibitions()
- random_exhibition()

## 위치 기반 근처 전시 추천

위치 기반 근처 전시 추천은 사용자의 현재 위치 정보를 기준으로 가까운 전시를 찾는 기능이다.

관련 endpoint는 다음과 같다.

GET /find_near_exhibition/

이 endpoint는 사용자의 위도와 경도 값을 입력받고, 전시 데이터의 위치 정보와 비교하여 가까운 전시를 탐색한다.

기본 처리 흐름은 다음과 같다.

1. 사용자 위치 입력
2. 전시 데이터 조회
3. 전시명, 위도, 경도 정보 구성
4. 사용자 위치와 전시 위치 비교
5. radius 기준으로 가까운 전시 탐색
6. 선택된 전시의 상세 정보 조회
7. 전시 추천 결과 반환

## 리플릿 결과 연결 전시 추천

모바일 리플릿 생성 기능에서도 전시 추천 정보가 함께 연결된다.

관련 endpoint는 다음과 같다.

POST /leaflet_creating/

리플릿 생성 과정에서는 추천 작품, 색상 정보, 감성 정보와 함께 전시 정보가 연결될 수 있다.

이 흐름에서는 `random_exhibition()` 함수가 사용되며, 리플릿 결과 안의 `recom_exhibition` 항목과 연결된다.

기본 처리 흐름은 다음과 같다.

1. 리플릿 생성 요청 처리
2. 사용자 이미지와 작품 후보 이미지 매칭
3. 색상 및 감성 기반 추천 작품 선정
4. 전시 후보 데이터 조회
5. 추천 전시 정보 선택
6. 리플릿 결과에 전시 정보 포함

## service module 역할

`exhibition_service.py`는 기존 backend prototype의 전시 추천 로직을 service layer로 분리하기 위한 파일이다.

주요 역할은 다음과 같다.

- 전시 데이터 조회 흐름 정리
- 사용자 위치 기반 전시 탐색 흐름 정리
- 전시 상세 정보 반환 흐름 정리
- route module과 기존 prototype logic 사이의 연결 구조 정리

## route module 역할

`exhibition_routes.py`는 전시 추천 endpoint를 route module 구조로 분리하기 위한 파일이다.

기존 실행 흐름은 prototype backend에 보존하면서, 전시 추천 API를 기능 단위로 관리할 수 있도록 정리한 구조다.

## schema module 역할

`exhibition_schema.py`는 전시 추천 기능에서 사용하는 요청 및 응답 구조를 정리하기 위한 파일이다.

전시 추천 기능은 위치 정보, 전시명, 전시 상세 정보, 추천 결과 구조와 연결된다.

## 구현 범위

현재 repository에서는 기존 backend prototype에 구현된 전시 추천 흐름을 보존하면서, 전시 추천 기능을 backend feature 단위로 정리한다.

전시 데이터의 전체 원본이나 내부 DB 값은 포함하지 않으며, 공개 가능한 source structure와 기능 흐름 중심으로 정리한다.

## 관련 문서

- docs/13-exhibition/exhibition-recommendation-flow.md
- docs/13-exhibition/nearby-exhibition-logic.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/12-mobile-leaflet/leaflet-result-structure.md
- docs/05-database/database-overview.md
