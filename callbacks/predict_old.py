import numpy as np
import pandas as pd
from dash import Input, Output, State, dcc
import dash_bootstrap_components as dbc
from myapp import app
import joblib
import plotly.express as px
import plotly.graph_objects as go

# Load the saved model
model = joblib.load('utils/best_xgb_model.pkl')

# Load your training dataset for plotting (replace with your actual path)
data = pd.read_csv("utils/data_site.csv")

# Example: assume it has columns ["bmi", "age", "label"]
# where label = 0 (no complications), 1 (complications)

@app.callback(
    [Output("prediction-output", "children"),
     Output("prediction-plot", "figure"),
     Output("prediction-plot-2", "figure")],
    Input("calcular-btn", "n_clicks"),
    State("input-age", "value"),
    State("input-sex", "value"),
    State("input-wgt", "value"),
    State("input-hgt", "value"),
    State("input-bmi", "value"),
    State("input-sbp", "value"),
    State("input-dbp", "value"),
    State("input-hdl", "value"),
    State("input-ldl", "value"),
    State("input-hf", "value"),
    State("input-smk_cur", "value"),
    State("input-t1d", "value"),
    prevent_initial_call=True
)
def predict(n_clicks, age, sex, wgt, hgt, bmi, sbp, dbp, hdl, ldl, hf, smk_cur, t1d):
    
    inputs_dict = {
        "age": age,
        "sex": sex,
        "wgt": wgt,
        "hgt": hgt,
        "bmi": bmi,
        "sbp": sbp,
        "dbp": dbp,
        "hdl": hdl,
        "ldl": ldl,
        "hf": hf,
        "smk_cur": smk_cur,
        "t1d": t1d
    }
    
    if any(value is None for value in inputs_dict.values()):
        return dbc.Alert("Please fill in all fields.", color="warning"), {}

    # Feature order must match training order
    feature_names = ['bmi', 'dbp', 'hdl', 'hf', 'hgt', 'ldl', 'sbp', 'smk_cur', 't1d', 'wgt', 'sex', 'age']
    inputs_ordered = [inputs_dict[col] for col in feature_names]
    
    features = pd.DataFrame([inputs_ordered], columns=feature_names)
    
    # Predict
    prediction = model.predict(features)[0]

    # Predict probability for class 1 (complication)
    probability = model.predict_proba(features)[0][1]
    
    # Message
    if prediction == 1:
        message = dbc.Alert(f"Result: Cardiovascular event likely ({probability:.1%} confidence)", color="danger")
    else:
        message = dbc.Alert(f"Result: Low risk of cardiovascular event ({1-probability:.1%} confidence)", color="success")
    
    # --- Plotting ---
    # Example: scatter Age vs BMI, colored by label
    # Map 0 -> No Event, 1 -> Event
    data["cv_event"] = data["y_cvdeath_6_months"].map({0: "No Event", 1: "Event"})

    fig1 = px.scatter(
        data, x="bmi", y="age", color="cv_event",
        opacity=0.6,
        title="BMI vs Age",
        labels={"cv_event": "6-Month Cardiovascular Death"},
        render_mode='svg'   # forces SVG
    )
    
    # Add new patient as a red star
    fig1.add_trace(go.Scatter(
        x=[bmi],
        y=[age],
        mode="markers",
        marker=dict(size=12, color="black", symbol="star"),
        name="New Patient"
    ))

    fig2 = px.scatter(
        data, x="sbp", y="dbp", color="cv_event",
        opacity=0.6,
        title="SBP vs DBP",
        labels={"cv_event": "6-Month Cardiovascular Death"},
        render_mode='svg'   # forces SVG
    )

    fig2.add_trace(go.Scatter(
        x=[sbp],
        y=[dbp],
        mode="markers",
        marker=dict(size=12, color="black", symbol="star"),
        name="New Patient"
    ))
    return message, fig1, fig2
