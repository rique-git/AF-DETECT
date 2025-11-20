
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

data = pd.read_csv("../data/Heart_Disease_Prediction_kaggle_data.csv")
data["Heart Disease"] = data["Heart Disease"].map({"Absence":0, "Presence": 1})
data = data.rename(columns={'EKG results': 'ECG results'})
data = data[data['ECG results'] != 1]

X = data.drop(columns=["Heart Disease"])
y = data["Heart Disease"]


rf_model = RandomForestClassifier()
rf_model.fit(X.values, y)

joblib.dump(rf_model, 'kaggle_model.pkl')