-- RestArt Example Seed Data
-- Non-sensitive sample records for local testing of the prototype SQL schema.

INSERT INTO users (user_id, nickname, email)
VALUES
    (1, 'sample_user', 'sample-user@example.com');

INSERT INTO artists (artist_id, nickname, name, bio)
VALUES
    (1, 'sample_artist', 'Sample Artist', 'Example artist profile for RestArt database testing.');

INSERT INTO emotion_dictionary (emotion_id, emotion_name, emotion_category, description)
VALUES
    (1, '행복', 'positive', '밝고 긍정적인 정서를 나타내는 감성'),
    (2, '평화', 'calm', '차분하고 안정적인 정서를 나타내는 감성'),
    (3, '호기심', 'exploration', '새로운 해석과 탐색을 유도하는 감성'),
    (4, '감각적', 'aesthetic', '시각적 자극과 미적 인상을 나타내는 감성');

INSERT INTO color_dictionary (
    color_id,
    color_name,
    rgb_r,
    rgb_g,
    rgb_b,
    tone_group,
    description,
    personality_text
)
VALUES
    (1, 'Cerulean', 59, 130, 157, 'blue', '푸른 계열의 차분한 색상', '차분하면서도 감각적인 분위기를 선호하는 사람입니다.'),
    (2, 'Yellow', 227, 189, 28, 'yellow', '밝고 따뜻한 노란 계열 색상', '밝고 생동감 있는 분위기에 끌리는 사람입니다.'),
    (3, 'Grey', 126, 126, 126, 'neutral', '중립적이고 안정적인 회색 계열 색상', '균형 있고 차분한 분위기를 선호하는 사람입니다.');

INSERT INTO artworks (
    artwork_id,
    artist_id,
    title,
    artist_name,
    image_url,
    description,
    main_color,
    status,
    source_type
)
VALUES
    (
        1,
        1,
        'Sample Artwork',
        'Sample Artist',
        'https://example.com/sample-artwork.jpg',
        'Example artwork record used for RestArt schema testing.',
        'Cerulean',
        'available',
        'artist'
    ),
    (
        2,
        NULL,
        'Recommendation Pool Artwork',
        'Recommendation Pool',
        'https://example.com/recommendation-artwork.jpg',
        'Example artwork used as a recommendation candidate.',
        'Yellow',
        'available',
        'recommendation_pool'
    );

INSERT INTO artwork_colors (
    artwork_id,
    color_name,
    rgb_r,
    rgb_g,
    rgb_b,
    ratio,
    cluster_count,
    cluster_order,
    is_main_color
)
VALUES
    (1, 'Cerulean', 59, 130, 157, 0.35000, 1, 1, TRUE),
    (1, 'Grey', 126, 126, 126, 0.18000, 1, 2, FALSE),
    (2, 'Yellow', 227, 189, 28, 0.42000, 1, 1, TRUE);

INSERT INTO artwork_emotions (
    artwork_id,
    emotion_id,
    emotion_name,
    emotion_rank,
    source
)
VALUES
    (1, 1, '행복', 1, 'ai'),
    (1, 3, '호기심', 2, 'ai'),
    (2, 1, '행복', 1, 'ai'),
    (2, 4, '감각적', 2, 'ai');

INSERT INTO expert_artworks (
    expert_artwork_id,
    title,
    image_url,
    color_summary
)
VALUES
    (
        1,
        'Sample Expert Artwork',
        'https://example.com/expert-artwork.jpg',
        JSON_OBJECT('colors', JSON_ARRAY('Cerulean', 'Grey'))
    );

INSERT INTO expert_interiors (
    expert_interior_id,
    expert_name,
    image_url,
    color_summary,
    linked_expert_artwork_id
)
VALUES
    (
        1,
        'Sample Interior Expert',
        'https://example.com/interior.jpg',
        JSON_OBJECT('colors', JSON_ARRAY('Cerulean', 'Grey')),
        1
    );

INSERT INTO user_space_images (
    space_image_id,
    user_id,
    image_url,
    dominant_rgb_r,
    dominant_rgb_g,
    dominant_rgb_b,
    color_summary
)
VALUES
    (
        1,
        1,
        'https://example.com/user-space.jpg',
        59,
        130,
        157,
        JSON_OBJECT('main_color', 'Cerulean')
    );

INSERT INTO recommendation_results (
    recommendation_id,
    user_id,
    space_image_id,
    artwork_id,
    emotion_match_count,
    kendall_tau_score,
    rank_order,
    recommendation_reason
)
VALUES
    (
        1,
        1,
        1,
        1,
        2,
        0.812300,
        1,
        'Matched by emotion count and color similarity.'
    );

INSERT INTO exhibitions (
    exhibition_id,
    title,
    organization,
    poster_url,
    description,
    location_name,
    latitude,
    longitude
)
VALUES
    (
        1,
        'Sample Exhibition',
        'Sample Gallery',
        'https://example.com/exhibition-poster.jpg',
        'Example exhibition record for leaflet testing.',
        'Sample Gallery Location',
        37.5665000,
        126.9780000
    );

INSERT INTO leaflet_sessions (
    leaflet_session_id,
    user_id,
    exhibition_id,
    dominant_color_name,
    dominant_rgb_r,
    dominant_rgb_g,
    dominant_rgb_b,
    personality_text
)
VALUES
    (
        1,
        1,
        1,
        'Cerulean',
        59,
        130,
        157,
        '차분하면서도 감각적인 분위기를 선호하는 사용자입니다.'
    );

INSERT INTO leaflet_images (
    leaflet_image_id,
    leaflet_session_id,
    uploaded_image_url,
    matched_artwork_id,
    selected_for_leaflet
)
VALUES
    (
        1,
        1,
        'https://example.com/leaflet-uploaded-image.jpg',
        1,
        TRUE
    );

INSERT INTO leaflet_recommendations (
    leaflet_recommendation_id,
    leaflet_session_id,
    recommendation_type,
    artwork_id,
    exhibition_id,
    rank_order,
    reason
)
VALUES
    (
        1,
        1,
        'artwork',
        1,
        NULL,
        1,
        'Recommended from the leaflet dominant color and artwork emotion match.'
    ),
    (
        2,
        1,
        'exhibition',
        NULL,
        1,
        1,
        'Recommended as a nearby or related exhibition.'
    );