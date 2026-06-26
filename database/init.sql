CREATE TABLE IF NOT EXISTS model_registry (
    id SERIAL PRIMARY KEY,
    model_name VARCHAR(100) NOT NULL,
    model_type VARCHAR(100),
    model_version VARCHAR(50),
    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS prediction_requests (
    id SERIAL PRIMARY KEY,
    request_id VARCHAR(100) UNIQUE NOT NULL,
    model_id INTEGER REFERENCES model_registry(id),

    environment VARCHAR(50),
    endpoint VARCHAR(100),
    input_data JSONB NOT NULL,

    status_code INTEGER,
    error_message TEXT,
    execution_time_ms FLOAT,

    created_at TIMESTAMP DEFAULT NOW()
);

CREATE TABLE IF NOT EXISTS prediction_results (
    id SERIAL PRIMARY KEY,
    request_id VARCHAR(100) REFERENCES prediction_requests(request_id),

    
    prediction INTEGER,
    probability FLOAT,
    threshold_used FLOAT,

    created_at TIMESTAMP DEFAULT NOW()
);