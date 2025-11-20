from dash import html, Input, Output, State, dcc
import dash_bootstrap_components as dbc

from myapp import app

@app.callback(
    Output("tab-content", "children"),
    Input("tabs", "active_tab")
)
def render_tab(tab):
    if tab == "geral":
        return html.Div([

            # --- Prediction selector and Time Interval selector ---
            dbc.Row([
                dbc.Col(
                    dbc.Select(
                        id="prediction-selector",
                        options=[
                            {"label": "Cardiovascular Death", "value": "cv_death"},
                            {"label": "Atrial Fibrillation", "value": "af"},
                            {"label": "Other Outcome", "value": "other"}
                        ],
                        value="cv_death",
                        className="mb-3"
                    ),
                    width=4
                ),

                dbc.Col(
                    dbc.Select(
                        id="time-interval-selector",
                        options=[
                            {"label": "1 month", "value": 1},
                            {"label": "3 months", "value": 3},
                            {"label": "6 months", "value": 6},
                            {"label": "1 year", "value": 12},
                            {"label": "2 years", "value": 24},
                            {"label": "5 years", "value": 60},
                        ],
                        value=6,  # default: 6 months
                        className="mb-3"
                    ),
                    width=2
                ),
            ], className="mb-3"),  # spacing below the row

            # --- Add/Remove input fields button ---
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        "Add/Remove Input Fields",
                        id="toggle-fields-btn",
                        color="info",
                        size="md",
                        className="mb-3"
                    ),
                    width="auto",
                    className="d-flex justify-content-left"
                )
            ),

            # --- Input fields ---
            dbc.Row([
                dbc.Col([dbc.Label("Age Range"), dcc.Dropdown(
                    id="input-age",
                    options=[
                        {"label": "40-49", "value": 0},
                        {"label": "50-59", "value": 1},
                        {"label": "60-69", "value": 2},
                        {"label": "70-79", "value": 3},
                        {"label": "80-89", "value": 4},
                        {"label": "90+", "value": 5}
                    ],
                    placeholder="Select age range"
                )], width=4),

                dbc.Col([dbc.Label("Sex"), dcc.Dropdown(
                    id="input-sex",
                    options=[
                        {"label": "Male", "value": 0},
                        {"label": "Female", "value": 1}
                    ],
                    value=0
                )], width=4),

                dbc.Col([dbc.Label("Weight (kg)"), dbc.Input(id="input-wgt", type="number", value=80)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Height (cm)"), dbc.Input(id="input-hgt", type="number", value=175)], width=4),
                dbc.Col([dbc.Label("BMI"), dbc.Input(id="input-bmi", type="number", value=25.5)], width=4),
                dbc.Col([dbc.Label("Systolic BP (SBP)"), dbc.Input(id="input-sbp", type="number", value=120)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Diastolic BP (DBP)"), dbc.Input(id="input-dbp", type="number", value=80)], width=4),
                dbc.Col([dbc.Label("HDL Cholesterol"), dbc.Input(id="input-hdl", type="number", value=45)], width=4),
                dbc.Col([dbc.Label("LDL Cholesterol"), dbc.Input(id="input-ldl", type="number", value=130)], width=4),
            ]),

            dbc.Row([
                dbc.Col([dbc.Label("Heart Failure History"), dcc.Dropdown(
                    id="input-hf",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),

                dbc.Col([dbc.Label("Current Smoker"), dcc.Dropdown(
                    id="input-smk_cur",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),

                dbc.Col([dbc.Label("Type 1 Diabetes"), dcc.Dropdown(
                    id="input-t1d",
                    options=[{"label": "Yes", "value": 1}, {"label": "No", "value": 0}],
                    value=0
                )], width=4),
            ]),

            # --- Calculate button ---
            dbc.Row(
                dbc.Col(
                    dbc.Button(
                        "Calculate",
                        id="calcular-btn",
                        color="secondary",  # neutral color
                        size="lg",
                        className="mt-3"
                    ),
                    width="auto",
                    className="d-flex justify-content-center"
                )
            ),

            # --- Output ---
            html.Div(id="prediction-output", className="mt-3"),

            # --- Graphs ---
            dcc.Graph(id="prediction-plot", className="mt-3", style={"height": "400px"}),
            dcc.Graph(id="prediction-plot-2", className="mt-3", style={"height": "400px"}),

        ])

    elif tab == "comp":
        return html.Div("Complications content...")

    elif tab == "sever":
        return html.Div("Severity content...")
