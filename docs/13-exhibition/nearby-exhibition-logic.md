# 근처 전시 추천 로직

이 문서는 RestArt backend prototype의 위치 기반 근처 전시 추천 로직을 정리한다.

근처 전시 추천 로직은 사용자의 현재 위치와 전시 데이터의 위치 정보를 비교하여, 설정된 반경 안에서 가까운 전시를 찾는 기능이다.

## 기능 목적

근처 전시 추천은 사용자가 현재 위치를 기준으로 방문 가능한 전시를 찾을 수 있도록 돕기 위한 기능이다.

RestArt는 작품 추천과 리플릿 생성 기능을 제공할 뿐 아니라, 추천 결과가 실제 전시 탐색으로 이어질 수 있도록 전시 위치 기반 추천 기능을 함께 사용한다.

## 관련 endpoint

GET /find_near_exhibition/

## 관련 source

- apps/backend/api-prototype/main.py
- apps/backend/api-prototype/exhibition.py
- apps/backend/api-prototype/services/exhibition_service.py
- apps/backend/api-prototype/routes/exhibition_routes.py
- apps/backend/api-prototype/schemas/exhibition_schema.py
- tools/recommendation-model/prototype/image_utils.py

## 관련 함수

근처 전시 추천 로직과 직접 연결되는 함수는 다음과 같다.

- find_nearby_exhibitions()
- find1_nearby_exhibitions()

## 입력 정보

근처 전시 추천 로직은 다음 정보를 사용한다.

- 사용자 위도
- 사용자 경도
- 전시명
- 전시 위도
- 전시 경도
- 검색 반경

backend prototype의 `/find_near_exhibition/` endpoint는 사용자 위치 정보를 입력받고, 전시 데이터의 위치 정보와 비교하여 추천 전시를 찾는다.

## 처리 흐름

근처 전시 추천 로직은 다음 순서로 동작한다.

1. 사용자 위치 입력
2. 전시 데이터 조회
3. 전시명, 위도, 경도 목록 구성
4. 사용자 위치 좌표 생성
5. 전시 위치와 사용자 위치 사이의 거리 비교
6. 설정된 반경 안의 전시 탐색
7. 가장 적합한 전시명 선택
8. 선택된 전시의 상세 정보 조회
9. 전시 추천 결과 반환

## 1. 사용자 위치 입력

사용자는 현재 위치를 나타내는 위도와 경도 값을 입력한다.

이 값은 사용자의 현재 위치 좌표로 사용되며, 전시 위치와의 거리 계산 기준이 된다.

## 2. 전시 데이터 조회

backend는 DB 또는 전시 데이터 source에서 전시 정보를 조회한다.

이 단계에서는 전시 추천에 필요한 전시명, 위도, 경도 정보를 중심으로 데이터를 구성한다.

## 3. 전시 위치 목록 구성

조회된 전시 데이터는 위치 비교가 가능한 형태로 정리된다.

전시 위치 목록에는 일반적으로 다음 정보가 포함된다.

- 전시명
- 전시 위도
- 전시 경도

## 4. 사용자 위치 좌표 생성

입력된 사용자 위도와 경도는 현재 위치 좌표로 변환된다.

이 좌표는 `find_nearby_exhibitions()` 또는 `find1_nearby_exhibitions()` 함수에서 전시 위치와 비교된다.

## 5. 거리 비교

시스템은 사용자 위치와 각 전시 위치 사이의 거리를 비교한다.

이 과정에서 설정된 반경 값이 기준으로 사용된다.

반경 안에 포함되는 전시는 근처 전시 후보가 된다.

## 6. 근처 전시 선택

전시 후보 중 조건에 맞는 전시를 선택한다.

prototype에서는 위치 정보와 반경 조건을 기준으로 전시명을 찾고, 이후 해당 전시명으로 상세 정보를 다시 조회하는 흐름을 가진다.

## 7. 전시 상세 정보 반환

선택된 전시명에 해당하는 상세 정보를 조회하여 추천 결과로 반환한다.

전시 상세 정보에는 전시 데이터 구조에 따라 다음 정보가 포함될 수 있다.

- 전시명
- 전시 위치
- 전시 설명
- 전시 이미지 또는 URL
- 전시 기간
- 전시 장소 정보

## 리플릿 기능과의 차이

근처 전시 추천 로직은 사용자의 위치를 기준으로 전시를 찾는다.

반면 모바일 리플릿 생성 기능에서 사용되는 전시 추천은 리플릿 결과에 전시 정보를 연결하기 위한 흐름이다.

| 구분      | 근처 전시 추천                                        | 리플릿 연결 전시 추천            |
| --------- | ----------------------------------------------------- | -------------------------------- |
| 기준      | 사용자 위치                                           | 리플릿 생성 결과                 |
| 입력      | 위도, 경도                                            | 리플릿 생성 과정의 전시 후보     |
| 주요 함수 | find_nearby_exhibitions(), find1_nearby_exhibitions() | random_exhibition()              |
| 결과      | 위치 기반 추천 전시                                   | 리플릿 결과에 포함되는 추천 전시 |

## 구현 범위

현재 repository에서는 기존 backend prototype에 포함된 위치 기반 전시 추천 로직을 문서화한다.

전체 전시 데이터 원본이나 내부 DB 값은 포함하지 않으며, 공개 가능한 코드 구조와 처리 흐름 중심으로 정리한다.

## 관련 문서

- apps/backend/exhibition/README.md
- docs/13-exhibition/exhibition-recommendation-flow.md
- docs/12-mobile-leaflet/mobile-leaflet-flow.md
- docs/12-mobile-leaflet/leaflet-result-structure.md
- docs/05-database/database-overview.md
