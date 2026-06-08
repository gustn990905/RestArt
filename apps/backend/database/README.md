# Backend Database Loaders

## 개요

이 폴더는 RestArt 백엔드에서 사용하는 작품 데이터 loader 파일을 정리한 공간이다.

RestArt는 작품 이미지, 작가명, 작품 설명, 감성 태그, 색상 클러스터 정보를 기반으로 사용자 공간에 어울리는 작품을 추천한다. 따라서 작품 데이터를 DB에 저장하는 loader는 추천 시스템의 기반 데이터 구축에 사용된다.

---

## 파일 구성

| 파일                               | 역할                                                       |
| ---------------------------------- | ---------------------------------------------------------- |
| `artist_artwork_loader.py`         | RestArt 참여 작가님들의 작품 데이터를 DB에 저장하는 loader |
| `recommendation_artwork_loader.py` | 추천 후보 작품 데이터를 DB에 저장하는 loader               |

---

## `artist_artwork_loader.py`

이 파일은 RestArt에 등록되는 작가 작품 데이터를 다룬다.

주요 데이터는 다음과 같다.

- 작품 이미지 URL
- 작품명
- 작가명
- 작품 설명
- 감성 태그
- 색상 클러스터 RGB
- 색상 비율
- 대표 색상

이 데이터는 플랫폼 내 작가 작품 DB를 구성하는 데 사용된다.

---

## `recommendation_artwork_loader.py`

이 파일은 추천 알고리즘이 비교 대상으로 사용하는 작품 데이터를 다룬다.

사용자가 공간 이미지를 업로드하면, 추천 알고리즘은 사용자 이미지에서 추출한 색상 및 감성 정보와 작품 DB의 정보를 비교한다.

이 파일은 그 추천 후보 작품 데이터를 DB에 저장하는 데 사용된다.

---

## DB 설정 방식

실제 DB 접속 정보는 코드에 직접 작성하지 않는다.

DB 연결 정보는 환경변수를 통해 관리한다.

필요한 환경변수는 다음과 같다.

```env
DB_HOST=localhost
DB_PORT=3306
DB_NAME=restartdb
DB_USER=root
DB_PASSWORD=
DB_CHARSET=utf8mb4
```
