from fastapi import FastAPI, HTTPException
from fastapi.responses import RedirectResponse
from pydantic import BaseModel
import pandas as pd

from app.schemas import PredictionInput
from app.model import model


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
    try:
        input_df = pd.DataFrame([data.model_dump()])

        probability = model.predict_proba(input_df)[0][1]
        prediction = int(probability >= THRESHOLD)

        return {
            "prediction": prediction,
            "probability": round(float(probability),4),
            "threshold" : THRESHOLD
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))