import os
import json
import uuid
import logging
from sqlalchemy import text
from app.database import engine

logger = logging.getLogger(__name__)


def log_prediction(
    input_data: dict,
    prediction: int | None,
    probability: float | None,
    threshold_used: float,
    execution_time_ms: float,
    status_code: int = 200,
    error_message: str | None = None,
    endpoint: str = "/predict",
):
    if engine is None:
        logger.info("Database logging skipped: DATABASE_URL is not defined.")
        return

    request_id = str(uuid.uuid4())
    active_model_id = os.getenv("ACTIVE_MODEL_ID")
    environment = os.getenv("DEPLOYMENT_TARGET")

    if active_model_id is None:
        raise ValueError("ACTIVE_MODEL_ID doit être défini quand DATABASE_URL est présent.")

    if environment is None:
        raise ValueError("DEPLOYMENT_TARGET doit être défini quand DATABASE_URL est présent.")

    model_id = int(active_model_id)

    try:
        with engine.begin() as conn:
            conn.execute(
                text("""
                    INSERT INTO prediction_requests (
                        request_id,
                        model_id,
                        environment,
                        endpoint,
                        input_data,
                        status_code,
                        error_message,
                        execution_time_ms
                    )
                    VALUES (
                        :request_id,
                        :model_id,
                        :environment,
                        :endpoint,
                        CAST(:input_data AS jsonb),
                        :status_code,
                        :error_message,
                        :execution_time_ms
                    )
                """),
                {
                    "request_id": request_id,
                    "model_id": model_id,
                    "environment": environment,
                    "endpoint": endpoint,
                    "input_data": json.dumps(input_data),
                    "status_code": status_code,
                    "error_message": error_message,
                    "execution_time_ms": execution_time_ms,
                },
            )

            conn.execute(
                text("""
                    INSERT INTO prediction_results (
                        request_id,
                        prediction,
                        probability,
                        threshold_used
                    )
                    VALUES (
                        :request_id,
                        :prediction,
                        :probability,
                        :threshold_used
                    )
                """),
                {
                    "request_id": request_id,
                    "prediction": prediction,
                    "probability": probability,
                    "threshold_used": threshold_used,
                },
            )

    except Exception as e:
        logger.warning(f"Database logging failed, prediction still returned: {e}")
        return