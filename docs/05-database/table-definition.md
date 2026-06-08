# Table Definition

## 개요

이 문서는 RestArt 데이터베이스의 주요 테이블과 각 테이블의 역할을 정의한다.

RestArt는 공간 기반 작품 추천과 전시 경험 기반 모바일 리플릿 기능을 하나의 플랫폼 안에서 제공한다.

따라서 DB는 다음 기능을 모두 지원해야 한다.

- 작가 작품 등록
- 작품 색상 분석
- 작품 감성 분석
- 공간 이미지 기반 작품 추천
- 전시 이미지 기반 리플릿 생성
- 전시 정보 관리
- 기준 색상 및 기준 감성 관리

---

## 테이블 그룹

RestArt DB는 다음 그룹으로 나눈다.

| 그룹             | 테이블                                                                               |
| ---------------- | ------------------------------------------------------------------------------------ |
| Core             | `users`, `artists`, `artworks`                                                       |
| Artwork Analysis | `artwork_colors`, `artwork_emotions`                                                 |
| Recommendation   | `user_space_images`, `recommendation_results`, `expert_interiors`, `expert_artworks` |
| Leaflet          | `leaflet_sessions`, `leaflet_images`, `leaflet_recommendations`                      |
| Exhibition       | `exhibitions`                                                                        |
| Reference        | `color_dictionary`, `emotion_dictionary`                                             |

---

## 1. `users`

서비스 사용자를 저장하는 테이블이다.

사용자는 공간 이미지를 업로드하고, 작품 추천을 받고, 컬렉션을 저장하고, 리플릿을 생성할 수 있다.

### 주요 컬럼

| 컬럼                | 설명                 |
| ------------------- | -------------------- |
| `user_id`           | 사용자 고유 ID       |
| `nickname`          | 사용자 닉네임        |
| `email`             | 사용자 이메일        |
| `profile_image_url` | 사용자 프로필 이미지 |
| `created_at`        | 가입일               |
| `updated_at`        | 수정일               |

---

## 2. `artists`

작가 정보를 저장하는 테이블이다.

RestArt에 작품을 등록하는 작가의 기본 정보를 관리한다.

### 주요 컬럼

| 컬럼                | 설명               |
| ------------------- | ------------------ |
| `artist_id`         | 작가 고유 ID       |
| `nickname`          | 작가 닉네임        |
| `name`              | 작가명             |
| `bio`               | 작가 소개          |
| `profile_image_url` | 작가 프로필 이미지 |
| `created_at`        | 등록일             |
| `updated_at`        | 수정일             |

---

## 3. `artworks`

작품의 기본 정보를 저장하는 핵심 테이블이다.

Day 4에서 정리한 기존 loader의 `url`, `title`, `author`, `description`, `main_color` 데이터를 이 테이블과 연결한다.

### 주요 컬럼

| 컬럼          | 설명                               |
| ------------- | ---------------------------------- |
| `artwork_id`  | 작품 고유 ID                       |
| `artist_id`   | 작가 ID                            |
| `title`       | 작품명                             |
| `artist_name` | 작가명 또는 작가 닉네임            |
| `image_url`   | 작품 이미지 URL                    |
| `description` | 작품 설명                          |
| `main_color`  | 대표 색상명                        |
| `price`       | 작품 가격                          |
| `status`      | 판매 상태                          |
| `source_type` | 작가 작품 또는 추천 후보 작품 구분 |
| `created_at`  | 등록일                             |
| `updated_at`  | 수정일                             |

### `source_type` 예시

| 값                    | 의미                   |
| --------------------- | ---------------------- |
| `artist`              | RestArt 참여 작가 작품 |
| `recommendation_pool` | 추천 후보 작품         |
| `exhibition`          | 전시 기반 작품         |

---

## 4. `artwork_colors`

작품에서 추출한 색상 정보를 저장하는 테이블이다.

K-means clustering 기반으로 추출된 RGB값, 색상 비율, 클러스터 정보를 저장한다.

### 주요 컬럼

| 컬럼               | 설명              |
| ------------------ | ----------------- |
| `artwork_color_id` | 작품 색상 고유 ID |
| `artwork_id`       | 작품 ID           |
| `color_name`       | 색상명            |
| `rgb_r`            | R 값              |
| `rgb_g`            | G 값              |
| `rgb_b`            | B 값              |
| `ratio`            | 작품 내 색상 비율 |
| `cluster_count`    | 클러스터 count    |
| `cluster_order`    | 색상 순서         |
| `is_main_color`    | 대표 색상 여부    |

---

## 5. `artwork_emotions`

작품별 감성 태그를 저장하는 테이블이다.

AI가 추출한 감성 또는 작가가 수정한 감성을 저장한다.

### 주요 컬럼

| 컬럼                 | 설명                   |
| -------------------- | ---------------------- |
| `artwork_emotion_id` | 작품 감성 고유 ID      |
| `artwork_id`         | 작품 ID                |
| `emotion_id`         | 감성 ID                |
| `emotion_name`       | 감성명                 |
| `emotion_rank`       | 감성 순위              |
| `source`             | AI 추출 또는 작가 수정 |
| `created_at`         | 생성일                 |

### `source` 예시

| 값       | 의미                         |
| -------- | ---------------------------- |
| `ai`     | AI 또는 멀티모달 모델이 추출 |
| `artist` | 작가가 수정 또는 추가        |
| `admin`  | 운영자가 보정                |

---

## 6. `color_dictionary`

RestArt 색상 기준 테이블이다.

Hue & Tone System 또는 자체 색상 테이블에 따라 대표 RGB와 색상명을 관리한다.

### 주요 컬럼

| 컬럼               | 설명                    |
| ------------------ | ----------------------- |
| `color_id`         | 색상 고유 ID            |
| `color_name`       | 색상명                  |
| `rgb_r`            | 대표 R 값               |
| `rgb_g`            | 대표 G 값               |
| `rgb_b`            | 대표 B 값               |
| `tone_group`       | 톤 그룹                 |
| `description`      | 색상 설명               |
| `personality_text` | 리플릿용 색상 성격 문구 |

---

## 7. `emotion_dictionary`

RestArt 감성 기준 테이블이다.

예술 작품 감상 시 느끼는 감성을 RestArt 자체 카테고리로 정리한 reference table이다.

### 주요 컬럼

| 컬럼               | 설명                |
| ------------------ | ------------------- |
| `emotion_id`       | 감성 고유 ID        |
| `emotion_name`     | 감성명              |
| `emotion_category` | 감성 분류           |
| `description`      | 감성 설명           |
| `source_reference` | 감성 정의 참고 기준 |

---

## 8. `user_space_images`

사용자가 업로드한 공간 이미지와 분석 결과를 저장하는 테이블이다.

공간 기반 작품 추천의 입력 데이터가 된다.

### 주요 컬럼

| 컬럼             | 설명                     |
| ---------------- | ------------------------ |
| `space_image_id` | 공간 이미지 고유 ID      |
| `user_id`        | 사용자 ID                |
| `image_url`      | 업로드된 공간 이미지 URL |
| `dominant_rgb_r` | 대표 R 값                |
| `dominant_rgb_g` | 대표 G 값                |
| `dominant_rgb_b` | 대표 B 값                |
| `color_summary`  | 추출 색상 요약           |
| `created_at`     | 업로드일                 |

---

## 9. `recommendation_results`

사용자 공간 이미지 기반 추천 결과를 저장하는 테이블이다.

추천 결과를 저장하면 나중에 사용자의 추천 이력을 확인하거나 추천 품질을 분석할 수 있다.

### 주요 컬럼

| 컬럼                    | 설명              |
| ----------------------- | ----------------- |
| `recommendation_id`     | 추천 결과 고유 ID |
| `user_id`               | 사용자 ID         |
| `space_image_id`        | 공간 이미지 ID    |
| `artwork_id`            | 추천 작품 ID      |
| `emotion_match_count`   | 감성 일치 개수    |
| `kendall_tau_score`     | 켄달타우 점수     |
| `rank_order`            | 추천 순위         |
| `recommendation_reason` | 추천 사유         |
| `created_at`            | 추천 생성일       |

---

## 10. `expert_interiors`

전문가 인테리어 DB를 저장하는 테이블이다.

사용자 공간 이미지와 비교할 기준 인테리어 데이터로 사용한다.

### 주요 컬럼

| 컬럼                       | 설명                       |
| -------------------------- | -------------------------- |
| `expert_interior_id`       | 전문가 인테리어 고유 ID    |
| `expert_name`              | 전문가명                   |
| `image_url`                | 인테리어 이미지 URL        |
| `color_summary`            | 색상 추출 요약             |
| `linked_expert_artwork_id` | 연결된 전문가 기준 작품 ID |

---

## 11. `expert_artworks`

전문가 인테리어와 연결된 기준 작품 데이터를 저장하는 테이블이다.

사용자 공간 이미지와 유사한 전문가 인테리어를 찾은 후, 해당 인테리어와 연결된 기준 작품을 찾는 데 사용한다.

### 주요 컬럼

| 컬럼                | 설명                |
| ------------------- | ------------------- |
| `expert_artwork_id` | 전문가 기준 작품 ID |
| `title`             | 작품명              |
| `image_url`         | 작품 이미지 URL     |
| `color_summary`     | 색상 추출 요약      |

---

## 12. `exhibitions`

전시 정보를 저장하는 테이블이다.

모바일 리플릿과 전시 추천 기능에서 사용한다.

### 주요 컬럼

| 컬럼            | 설명                        |
| --------------- | --------------------------- |
| `exhibition_id` | 전시 고유 ID                |
| `title`         | 전시명                      |
| `organization`  | 전시 기관                   |
| `poster_url`    | 전시 포스터 또는 이미지 URL |
| `description`   | 전시 소개                   |
| `location_name` | 전시 장소                   |
| `latitude`      | 위도                        |
| `longitude`     | 경도                        |
| `start_date`    | 전시 시작일                 |
| `end_date`      | 전시 종료일                 |
| `created_at`    | 등록일                      |

---

## 13. `leaflet_sessions`

사용자의 리플릿 생성 단위를 저장하는 테이블이다.

사용자가 전시장에서 촬영한 여러 이미지를 하나의 리플릿 세션으로 묶는다.

### 주요 컬럼

| 컬럼                  | 설명                |
| --------------------- | ------------------- |
| `leaflet_session_id`  | 리플릿 세션 ID      |
| `user_id`             | 사용자 ID           |
| `exhibition_id`       | 전시 ID             |
| `dominant_color_name` | 리플릿 대표 색상명  |
| `dominant_rgb_r`      | 대표 R 값           |
| `dominant_rgb_g`      | 대표 G 값           |
| `dominant_rgb_b`      | 대표 B 값           |
| `personality_text`    | 색상 기반 성격 문구 |
| `created_at`          | 생성일              |

---

## 14. `leaflet_images`

리플릿 생성에 사용된 촬영 이미지를 저장하는 테이블이다.

촬영 이미지가 어떤 작품과 매핑되었는지 저장한다.

### 주요 컬럼

| 컬럼                   | 설명                         |
| ---------------------- | ---------------------------- |
| `leaflet_image_id`     | 리플릿 이미지 ID             |
| `leaflet_session_id`   | 리플릿 세션 ID               |
| `uploaded_image_url`   | 사용자가 촬영한 이미지 URL   |
| `matched_artwork_id`   | 매핑된 작품 ID               |
| `selected_for_leaflet` | 리플릿 대표 이미지 선정 여부 |
| `created_at`           | 생성일                       |

---

## 15. `leaflet_recommendations`

리플릿 결과에서 추천된 작품과 전시 정보를 저장하는 테이블이다.

### 주요 컬럼

| 컬럼                        | 설명                     |
| --------------------------- | ------------------------ |
| `leaflet_recommendation_id` | 리플릿 추천 ID           |
| `leaflet_session_id`        | 리플릿 세션 ID           |
| `recommendation_type`       | 작품 추천 또는 전시 추천 |
| `artwork_id`                | 추천 작품 ID             |
| `exhibition_id`             | 추천 전시 ID             |
| `rank_order`                | 추천 순위                |
| `reason`                    | 추천 사유                |
| `created_at`                | 생성일                   |

---

## 정리

RestArt DB는 작품 DB를 중심으로 구성된다.

작품 데이터는 색상, 감성, 추천, 리플릿, 전시 기능과 연결되며, 공간 기반 작품 추천과 모바일 리플릿 기능 모두에서 공통 기반 데이터로 활용된다.
