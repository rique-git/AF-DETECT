from fastapi import APIRouter
from pydantic import BaseModel
import joblib
import pandas as pd
import xgboost as xgb

from app.config import MODEL_PATH


_model = None

feature_names = [
    'bmi', 'dbp', 'hdl', 'hf', 'hgt',
    'ldl', 'sbp', 'smk_cur', 't1d', 'wgt', 'sex', 'age'
]

def get_model():

    global _model
    if _model is None:
        _model = xgb.XGBClassifier()
        _model.load_model(MODEL_PATH)
    return _model


router = APIRouter()


class PatientData(BaseModel):

    age: float
    sex: int
    wgt: float
    hgt: float
    bmi: float
    sbp: float
    dbp: float
    hdl: float
    ldl: float
    hf: int
    smk_cur: int
    t1d: int

class PredictionResponse(BaseModel):

    prediction: int
    probability: float


@router.post(
    "/predict",
    response_model=PredictionResponse
)

def predict(data: PatientData):

    model = get_model()

    feature_names = [
        "bmi", "dbp", "hdl", "hf", "hgt",
        "ldl", "sbp", "smk_cur", "t1d",
        "wgt", "sex", "age"
    ]

    inputs_dict = data.dict()

    inputs_ordered = [
        inputs_dict[col] for col in feature_names
    ]

    features = pd.DataFrame(
        [inputs_ordered],
        columns=feature_names
    )

    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])

    return {
        "prediction": prediction,
        "probability": probability
    }
