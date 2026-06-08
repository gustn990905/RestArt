-- RestArt Initial Database Schema
-- Prototype/test schema derived from the backend artwork loader and recommendation data flow.
-- This SQL schema is used to document and test the backend recommendation prototype.

CREATE TABLE IF NOT EXISTS users (
    user_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL,
    email VARCHAR(255) UNIQUE,
    profile_image_url TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS artists (
    artist_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    nickname VARCHAR(100) NOT NULL,
    name VARCHAR(100),
    bio TEXT,
    profile_image_url TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS emotion_dictionary (
    emotion_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    emotion_name VARCHAR(100) NOT NULL UNIQUE,
    emotion_category VARCHAR(100),
    description TEXT,
    source_reference TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS color_dictionary (
    color_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    color_name VARCHAR(100) NOT NULL,
    rgb_r INT NOT NULL,
    rgb_g INT NOT NULL,
    rgb_b INT NOT NULL,
    tone_group VARCHAR(100),
    description TEXT,
    personality_text TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS artworks (
    artwork_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    artist_id BIGINT NULL,
    title VARCHAR(255) NOT NULL,
    artist_name VARCHAR(100),
    image_url TEXT NOT NULL,
    description TEXT,
    main_color VARCHAR(100),
    price DECIMAL(12,2),
    status VARCHAR(50) DEFAULT 'available',
    source_type VARCHAR(50) DEFAULT 'artist',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    updated_at DATETIME DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
    CONSTRAINT fk_artworks_artist
        FOREIGN KEY (artist_id)
        REFERENCES artists(artist_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS artwork_colors (
    artwork_color_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    artwork_id BIGINT NOT NULL,
    color_name VARCHAR(100),
    rgb_r INT NOT NULL,
    rgb_g INT NOT NULL,
    rgb_b INT NOT NULL,
    ratio DECIMAL(8,5),
    cluster_count INT,
    cluster_order INT,
    is_main_color BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_artwork_colors_artwork
        FOREIGN KEY (artwork_id)
        REFERENCES artworks(artwork_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS artwork_emotions (
    artwork_emotion_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    artwork_id BIGINT NOT NULL,
    emotion_id BIGINT NULL,
    emotion_name VARCHAR(100) NOT NULL,
    emotion_rank INT,
    source VARCHAR(50) DEFAULT 'ai',
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_artwork_emotions_artwork
        FOREIGN KEY (artwork_id)
        REFERENCES artworks(artwork_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_artwork_emotions_emotion
        FOREIGN KEY (emotion_id)
        REFERENCES emotion_dictionary(emotion_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS expert_artworks (
    expert_artwork_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    image_url TEXT NOT NULL,
    color_summary JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS expert_interiors (
    expert_interior_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    expert_name VARCHAR(100),
    image_url TEXT NOT NULL,
    color_summary JSON,
    linked_expert_artwork_id BIGINT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_expert_interiors_artwork
        FOREIGN KEY (linked_expert_artwork_id)
        REFERENCES expert_artworks(expert_artwork_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS user_space_images (
    space_image_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NULL,
    image_url TEXT NOT NULL,
    dominant_rgb_r INT,
    dominant_rgb_g INT,
    dominant_rgb_b INT,
    color_summary JSON,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_user_space_images_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS recommendation_results (
    recommendation_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NULL,
    space_image_id BIGINT NULL,
    artwork_id BIGINT NOT NULL,
    emotion_match_count INT DEFAULT 0,
    kendall_tau_score DECIMAL(10,6),
    rank_order INT NOT NULL,
    recommendation_reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_recommendation_results_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE SET NULL,
    CONSTRAINT fk_recommendation_results_space_image
        FOREIGN KEY (space_image_id)
        REFERENCES user_space_images(space_image_id)
        ON DELETE SET NULL,
    CONSTRAINT fk_recommendation_results_artwork
        FOREIGN KEY (artwork_id)
        REFERENCES artworks(artwork_id)
        ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS exhibitions (
    exhibition_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255) NOT NULL,
    organization VARCHAR(255),
    poster_url TEXT,
    description TEXT,
    location_name VARCHAR(255),
    latitude DECIMAL(10,7),
    longitude DECIMAL(10,7),
    start_date DATE,
    end_date DATE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS leaflet_sessions (
    leaflet_session_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    user_id BIGINT NULL,
    exhibition_id BIGINT NULL,
    dominant_color_name VARCHAR(100),
    dominant_rgb_r INT,
    dominant_rgb_g INT,
    dominant_rgb_b INT,
    personality_text TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_leaflet_sessions_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
        ON DELETE SET NULL,
    CONSTRAINT fk_leaflet_sessions_exhibition
        FOREIGN KEY (exhibition_id)
        REFERENCES exhibitions(exhibition_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS leaflet_images (
    leaflet_image_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    leaflet_session_id BIGINT NOT NULL,
    uploaded_image_url TEXT NOT NULL,
    matched_artwork_id BIGINT NULL,
    selected_for_leaflet BOOLEAN DEFAULT FALSE,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_leaflet_images_session
        FOREIGN KEY (leaflet_session_id)
        REFERENCES leaflet_sessions(leaflet_session_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_leaflet_images_artwork
        FOREIGN KEY (matched_artwork_id)
        REFERENCES artworks(artwork_id)
        ON DELETE SET NULL
);

CREATE TABLE IF NOT EXISTS leaflet_recommendations (
    leaflet_recommendation_id BIGINT AUTO_INCREMENT PRIMARY KEY,
    leaflet_session_id BIGINT NOT NULL,
    recommendation_type VARCHAR(50) NOT NULL,
    artwork_id BIGINT NULL,
    exhibition_id BIGINT NULL,
    rank_order INT,
    reason TEXT,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT fk_leaflet_recommendations_session
        FOREIGN KEY (leaflet_session_id)
        REFERENCES leaflet_sessions(leaflet_session_id)
        ON DELETE CASCADE,
    CONSTRAINT fk_leaflet_recommendations_artwork
        FOREIGN KEY (artwork_id)
        REFERENCES artworks(artwork_id)
        ON DELETE SET NULL,
    CONSTRAINT fk_leaflet_recommendations_exhibition
        FOREIGN KEY (exhibition_id)
        REFERENCES exhibitions(exhibition_id)
        ON DELETE SET NULL
);