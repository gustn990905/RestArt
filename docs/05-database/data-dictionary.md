# Data Dictionary

## 개요

이 문서는 RestArt 데이터베이스의 주요 테이블과 컬럼 정의를 정리한다.

Data Dictionary는 각 테이블의 컬럼명, 데이터 타입, 설명, 비고를 기록하는 문서이다. 개발자는 이 문서를 기준으로 API 응답 구조, DB schema, 추천 알고리즘 입력값을 맞출 수 있다.

---

## 1. `users`

서비스 사용자를 저장한다.

| 컬럼                | 타입         | 설명                     | 비고        |
| ------------------- | ------------ | ------------------------ | ----------- |
| `user_id`           | BIGINT       | 사용자 고유 ID           | Primary Key |
| `nickname`          | VARCHAR(100) | 사용자 닉네임            |             |
| `email`             | VARCHAR(255) | 사용자 이메일            | Unique      |
| `profile_image_url` | TEXT         | 사용자 프로필 이미지 URL | Nullable    |
| `created_at`        | DATETIME     | 생성일                   |             |
| `updated_at`        | DATETIME     | 수정일                   |             |

---

## 2. `artists`

작가 정보를 저장한다.

| 컬럼                | 타입         | 설명                   | 비고        |
| ------------------- | ------------ | ---------------------- | ----------- |
| `artist_id`         | BIGINT       | 작가 고유 ID           | Primary Key |
| `nickname`          | VARCHAR(100) | 작가 닉네임            |             |
| `name`              | VARCHAR(100) | 작가명                 | Nullable    |
| `bio`               | TEXT         | 작가 소개              | Nullable    |
| `profile_image_url` | TEXT         | 작가 프로필 이미지 URL | Nullable    |
| `created_at`        | DATETIME     | 생성일                 |             |
| `updated_at`        | DATETIME     | 수정일                 |             |

---

## 3. `artworks`

작품의 기본 정보를 저장한다.

기존 loader 코드의 `images` 테이블 구조를 분리하여 `artworks`, `artwork_colors`, `artwork_emotions`로 확장한다.

| 컬럼          | 타입          | 설명                    | 비고                                    |
| ------------- | ------------- | ----------------------- | --------------------------------------- |
| `artwork_id`  | BIGINT        | 작품 고유 ID            | Primary Key                             |
| `artist_id`   | BIGINT        | 작가 ID                 | Foreign Key                             |
| `title`       | VARCHAR(255)  | 작품명                  |                                         |
| `artist_name` | VARCHAR(100)  | 작가명 또는 작가 닉네임 | 기존 loader의 `author`                  |
| `image_url`   | TEXT          | 작품 이미지 URL         | 기존 loader의 `url`                     |
| `description` | TEXT          | 작품 설명               | 기존 loader의 `description`             |
| `main_color`  | VARCHAR(100)  | 대표 색상명             | 기존 loader의 `main_color`              |
| `price`       | DECIMAL(12,2) | 작품 가격               | Nullable                                |
| `status`      | VARCHAR(50)   | 판매 상태               | 예: available, sold, hidden             |
| `source_type` | VARCHAR(50)   | 작품 데이터 출처        | artist, recommendation_pool, exhibition |
| `created_at`  | DATETIME      | 생성일                  |                                         |
| `updated_at`  | DATETIME      | 수정일                  |                                         |

---

## 4. `artwork_colors`

작품별 색상 추출 결과를 저장한다.

K-means clustering을 통해 추출된 RGB 값, 색상 비율, 클러스터 정보를 관리한다.

| 컬럼               | 타입         | 설명              | 비고        |
| ------------------ | ------------ | ----------------- | ----------- |
| `artwork_color_id` | BIGINT       | 작품 색상 고유 ID | Primary Key |
| `artwork_id`       | BIGINT       | 작품 ID           | Foreign Key |
| `color_name`       | VARCHAR(100) | 색상명            |             |
| `rgb_r`            | INT          | Red 값            | 0~255       |
| `rgb_g`            | INT          | Green 값          | 0~255       |
| `rgb_b`            | INT          | Blue 값           | 0~255       |
| `ratio`            | DECIMAL(8,5) | 작품 내 색상 비율 |             |
| `cluster_count`    | INT          | 클러스터 count    |             |
| `cluster_order`    | INT          | 색상 순서         |             |
| `is_main_color`    | BOOLEAN      | 대표 색상 여부    |             |

---

## 5. `artwork_emotions`

작품별 감성 태그를 저장한다.

AI가 추출한 감성, 작가가 수정한 감성, 운영자가 보정한 감성을 함께 저장할 수 있다.

| 컬럼                 | 타입         | 설명              | 비고              |
| -------------------- | ------------ | ----------------- | ----------------- |
| `artwork_emotion_id` | BIGINT       | 작품 감성 고유 ID | Primary Key       |
| `artwork_id`         | BIGINT       | 작품 ID           | Foreign Key       |
| `emotion_id`         | BIGINT       | 감성 ID           | Foreign Key       |
| `emotion_name`       | VARCHAR(100) | 감성명            |                   |
| `emotion_rank`       | INT          | 감성 순위         | 1~3               |
| `source`             | VARCHAR(50)  | 감성 생성 출처    | ai, artist, admin |
| `created_at`         | DATETIME     | 생성일            |                   |

---

## 6. `color_dictionary`

RestArt 색상 기준 테이블이다.

Hue & Tone System, Tailwind 색상 범위, 자체 색상 매핑을 기반으로 색상명을 관리한다.

| 컬럼               | 타입         | 설명                    | 비고        |
| ------------------ | ------------ | ----------------------- | ----------- |
| `color_id`         | BIGINT       | 색상 고유 ID            | Primary Key |
| `color_name`       | VARCHAR(100) | 색상명                  |             |
| `rgb_r`            | INT          | 대표 Red 값             | 0~255       |
| `rgb_g`            | INT          | 대표 Green 값           | 0~255       |
| `rgb_b`            | INT          | 대표 Blue 값            | 0~255       |
| `tone_group`       | VARCHAR(100) | 톤 그룹                 | Nullable    |
| `description`      | TEXT         | 색상 설명               | Nullable    |
| `personality_text` | TEXT         | 리플릿용 색상 성격 문구 | Nullable    |

---

## 7. `emotion_dictionary`

RestArt 감성 기준 테이블이다.

예술 작품 감상 시 느끼는 감성을 RestArt 자체 감성 카테고리로 정리한다.

| 컬럼               | 타입         | 설명                | 비고        |
| ------------------ | ------------ | ------------------- | ----------- |
| `emotion_id`       | BIGINT       | 감성 고유 ID        | Primary Key |
| `emotion_name`     | VARCHAR(100) | 감성명              |             |
| `emotion_category` | VARCHAR(100) | 감성 분류           |             |
| `description`      | TEXT         | 감성 설명           | Nullable    |
| `source_reference` | TEXT         | 감성 정의 참고 기준 | Nullable    |

---

## 8. `user_space_images`

사용자가 업로드한 공간 이미지와 분석 결과를 저장한다.

| 컬럼             | 타입     | 설명                        | 비고        |
| ---------------- | -------- | --------------------------- | ----------- |
| `space_image_id` | BIGINT   | 공간 이미지 고유 ID         | Primary Key |
| `user_id`        | BIGINT   | 사용자 ID                   | Foreign Key |
| `image_url`      | TEXT     | 공간 이미지 URL             |             |
| `dominant_rgb_r` | INT      | 대표 Red 값                 | Nullable    |
| `dominant_rgb_g` | INT      | 대표 Green 값               | Nullable    |
| `dominant_rgb_b` | INT      | 대표 Blue 값                | Nullable    |
| `color_summary`  | JSON     | K-means 기반 색상 분석 결과 | Nullable    |
| `created_at`     | DATETIME | 업로드일                    |             |

---

## 9. `recommendation_results`

공간 이미지 기반 작품 추천 결과를 저장한다.

| 컬럼                    | 타입          | 설명              | 비고        |
| ----------------------- | ------------- | ----------------- | ----------- |
| `recommendation_id`     | BIGINT        | 추천 결과 고유 ID | Primary Key |
| `user_id`               | BIGINT        | 사용자 ID         | Foreign Key |
| `space_image_id`        | BIGINT        | 공간 이미지 ID    | Foreign Key |
| `artwork_id`            | BIGINT        | 추천 작품 ID      | Foreign Key |
| `emotion_match_count`   | INT           | 감성 일치 개수    | 0~3         |
| `kendall_tau_score`     | DECIMAL(10,6) | 켄달타우 점수     | Nullable    |
| `rank_order`            | INT           | 추천 순위         |             |
| `recommendation_reason` | TEXT          | 추천 사유         | Nullable    |
| `created_at`            | DATETIME      | 추천 생성일       |             |

---

## 10. `expert_interiors`

전문가 인테리어 기준 데이터를 저장한다.

사용자 공간 이미지와 비교할 기준 인테리어 역할을 한다.

| 컬럼                       | 타입         | 설명                       | 비고        |
| -------------------------- | ------------ | -------------------------- | ----------- |
| `expert_interior_id`       | BIGINT       | 전문가 인테리어 ID         | Primary Key |
| `expert_name`              | VARCHAR(100) | 전문가명                   | Nullable    |
| `image_url`                | TEXT         | 인테리어 이미지 URL        |             |
| `color_summary`            | JSON         | 인테리어 색상 분석 결과    |             |
| `linked_expert_artwork_id` | BIGINT       | 연결된 전문가 기준 작품 ID | Foreign Key |

---

## 11. `expert_artworks`

전문가 인테리어와 연결된 기준 작품 데이터를 저장한다.

| 컬럼                | 타입         | 설명                | 비고        |
| ------------------- | ------------ | ------------------- | ----------- |
| `expert_artwork_id` | BIGINT       | 전문가 기준 작품 ID | Primary Key |
| `title`             | VARCHAR(255) | 작품명              |             |
| `image_url`         | TEXT         | 작품 이미지 URL     |             |
| `color_summary`     | JSON         | 작품 색상 분석 결과 |             |

---

## 12. `exhibitions`

전시 정보를 저장한다.

| 컬럼            | 타입          | 설명                        | 비고        |
| --------------- | ------------- | --------------------------- | ----------- |
| `exhibition_id` | BIGINT        | 전시 고유 ID                | Primary Key |
| `title`         | VARCHAR(255)  | 전시명                      |             |
| `organization`  | VARCHAR(255)  | 전시 기관                   |             |
| `poster_url`    | TEXT          | 전시 포스터 또는 이미지 URL | Nullable    |
| `description`   | TEXT          | 전시 소개                   | Nullable    |
| `location_name` | VARCHAR(255)  | 전시 장소                   | Nullable    |
| `latitude`      | DECIMAL(10,7) | 위도                        | Nullable    |
| `longitude`     | DECIMAL(10,7) | 경도                        | Nullable    |
| `start_date`    | DATE          | 전시 시작일                 | Nullable    |
| `end_date`      | DATE          | 전시 종료일                 | Nullable    |
| `created_at`    | DATETIME      | 등록일                      |             |

---

## 13. `leaflet_sessions`

사용자의 리플릿 생성 단위를 저장한다.

| 컬럼                  | 타입         | 설명                | 비고        |
| --------------------- | ------------ | ------------------- | ----------- |
| `leaflet_session_id`  | BIGINT       | 리플릿 세션 ID      | Primary Key |
| `user_id`             | BIGINT       | 사용자 ID           | Foreign Key |
| `exhibition_id`       | BIGINT       | 전시 ID             | Foreign Key |
| `dominant_color_name` | VARCHAR(100) | 리플릿 대표 색상명  | Nullable    |
| `dominant_rgb_r`      | INT          | 대표 Red 값         | Nullable    |
| `dominant_rgb_g`      | INT          | 대표 Green 값       | Nullable    |
| `dominant_rgb_b`      | INT          | 대표 Blue 값        | Nullable    |
| `personality_text`    | TEXT         | 색상 기반 성격 문구 | Nullable    |
| `created_at`          | DATETIME     | 생성일              |             |

---

## 14. `leaflet_images`

리플릿 생성에 사용된 촬영 이미지를 저장한다.

| 컬럼                   | 타입     | 설명                         | 비고        |
| ---------------------- | -------- | ---------------------------- | ----------- |
| `leaflet_image_id`     | BIGINT   | 리플릿 이미지 ID             | Primary Key |
| `leaflet_session_id`   | BIGINT   | 리플릿 세션 ID               | Foreign Key |
| `uploaded_image_url`   | TEXT     | 사용자가 촬영한 이미지 URL   |             |
| `matched_artwork_id`   | BIGINT   | 매핑된 작품 ID               | Foreign Key |
| `selected_for_leaflet` | BOOLEAN  | 리플릿 대표 이미지 선정 여부 |             |
| `created_at`           | DATETIME | 생성일                       |             |

---

## 15. `leaflet_recommendations`

리플릿 결과에서 추천된 작품과 전시를 저장한다.

| 컬럼                        | 타입        | 설명           | 비고                |
| --------------------------- | ----------- | -------------- | ------------------- |
| `leaflet_recommendation_id` | BIGINT      | 리플릿 추천 ID | Primary Key         |
| `leaflet_session_id`        | BIGINT      | 리플릿 세션 ID | Foreign Key         |
| `recommendation_type`       | VARCHAR(50) | 추천 유형      | artwork, exhibition |
| `artwork_id`                | BIGINT      | 추천 작품 ID   | Nullable            |
| `exhibition_id`             | BIGINT      | 추천 전시 ID   | Nullable            |
| `rank_order`                | INT         | 추천 순위      |                     |
| `reason`                    | TEXT        | 추천 사유      | Nullable            |
| `created_at`                | DATETIME    | 생성일         |                     |

---

## 정리

이 Data Dictionary는 5단계의 `schema.sql` 작성 기준으로 사용한다.

향후 실제 운영 단계에서는 컬럼 제약조건, 인덱스, nullable 여부, foreign key 제약조건을 더 구체화할 수 있다.

