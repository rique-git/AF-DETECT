from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Load model
model = joblib.load("utils/best_xgb_model.pkl")

# Define input schema
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

app = FastAPI()

@app.post("/predict")
def predict(data: PatientData):
    # Must respect training feature order
    feature_names = ['bmi', 'dbp', 'hdl', 'hf', 'hgt',
                     'ldl', 'sbp', 'smk_cur', 't1d', 'wgt', 'sex', 'age']
    
    inputs_dict = data.dict()
    inputs_ordered = [inputs_dict[col] for col in feature_names]
    features = pd.DataFrame([inputs_ordered], columns=feature_names)
    
    prediction = int(model.predict(features)[0])
    probability = float(model.predict_proba(features)[0][1])
    
    return {"prediction": prediction, "probability": probability}
