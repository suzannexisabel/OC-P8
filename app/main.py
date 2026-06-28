from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
import pandas as pd
import time

from app.schemas import PredictionInput
from app.model import model
from app.monitoring_logger import log_prediction


app = FastAPI(
    title="API de scoring crédit",
    description="API MLOps permettant de prédire le risque de défaut d’un client à partir de données applicatives, bureau et historiques.",
    version="1.0.0"
)

THRESHOLD = 0.54

@app.get("/")
def root():
    return RedirectResponse(url="/docs")


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post(
        "/predict",
        summary="Prédire le risque de défaut client",
        description="Retourne une prédiction binaire et une probabilité de défaut à partir des caractéristiques client."
        )

def predict(data: PredictionInput):
    start_time = time.perf_counter()
    input_data = data.model_dump()

    prediction = None
    probability = None

    try:
        input_df = pd.DataFrame([input_data])

        probability = float(model.predict_proba(input_df)[0][1])
        prediction = int(probability >= THRESHOLD)

        execution_time_ms = (time.perf_counter() - start_time) * 1000

        log_prediction(
            input_data=input_data,
            prediction=prediction,
            probability=probability,
            threshold_used=THRESHOLD,
            execution_time_ms=execution_time_ms,
            status_code=200,
        )

        return {
            "prediction": prediction,
            "probability": round(float(probability),4),
            "threshold" : THRESHOLD
        }

    except Exception as e:
        execution_time_ms = (time.perf_counter() - start_time) * 1000

        log_prediction(
            input_data=input_data,
            prediction=prediction,
            probability=probability,
            threshold_used=THRESHOLD,
            execution_time_ms=execution_time_ms,
            status_code=500,
            error_message=str(e),
        )

        raise HTTPException(status_code=500, detail=str(e))