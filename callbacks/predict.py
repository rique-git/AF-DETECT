import requests
import pandas as pd
from dash import Input, Output, State, dcc, html
import dash_bootstrap_components as dbc
from myapp import app
import plotly.express as px
import plotly.graph_objects as go

# Load training data for plots
data = pd.read_csv("utils/data_site.csv")

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
        return dbc.Alert("Please fill in all fields.", color="warning"), {}, {}

    # Call API
    res = requests.post("http://127.0.0.1:8000/predict", json=inputs_dict)
    if res.status_code != 200:
        return dbc.Alert("Error: Could not connect to prediction API.", color="danger"), {}, {}

    api_result = res.json()
    prediction = api_result["prediction"]
    probability = api_result["probability"]

    # Message
    if prediction == 1:
        message = dbc.Alert(f"Result: Cardiovascular event likely ({probability:.1%} confidence)", color="danger")
    else:
        message = dbc.Alert(f"Result: Low risk of cardiovascular event ({1-probability:.1%} confidence)", color="success")

    # --- Plots ---
    data["cv_event"] = data["y_cvdeath_6_months"].map({0: "No Event", 1: "Event"})

    age_labels = {
        0: "40-49",
        1: "50-59",
        2: "60-69",
        3: "70-79",
        4: "80-89",
        5: "90+"
    }
    age_labels_order = ['90+', '80-89', '70-79', '60-69', '50-59', '40-49']

    data_plot = data.copy()
    data_plot["age"] = data_plot["age"].map(age_labels)
    data_plot["age"] = pd.Categorical(
        data_plot["age"], 
        categories=age_labels_order, 
        ordered=True
    )


    fig1 = px.scatter(
        data_plot, x="bmi", y="age", color="cv_event",
        opacity=0.6,
        title="BMI vs Age",
        labels={"cv_event": "6-Month Cardiovascular Death"},
        render_mode='svg',
        category_orders={"age": age_labels_order},
    )
    fig1.add_trace(go.Scatter(
        x=[bmi], y=[age_labels[age]], mode="markers",
        marker=dict(size=12, color="black", symbol="star"),
        name="New Patient"
    ))

    fig2 = px.scatter(
        data_plot, x="sbp", y="dbp", color="cv_event",
        opacity=0.6,
        title="SBP vs DBP",
        labels={"cv_event": "6-Month Cardiovascular Death"},
        render_mode='svg'
    )
    fig2.add_trace(go.Scatter(
        x=[sbp], y=[dbp], mode="markers",
        marker=dict(size=12, color="black", symbol="star"),
        name="New Patient"
    ))

    fig1.update_layout(
        autosize=True,
        margin=dict(l=40, r=40, t=40, b=40),
        height=400  # optional fixed height
    )

    fig2.update_layout(
        autosize=True,
        margin=dict(l=40, r=40, t=40, b=40),
        height=400
    )

    return message, fig1, fig2
