from dash import html, Input, Output
import dash_bootstrap_components as dbc


def register(app):

    @app.callback(
        Output("page-content", "children"),
        Input("url", "pathname")
    )
    def display_page(pathname):

        if pathname == "/inicio" or pathname == "/":
            return html.Div([

                html.Div(
                    [
                        html.H1("Welcome to", className="mb-0"),
                        html.Img(
                            src="/assets/images/logo.jpg",
                            height="80px",
                            style={"marginLeft": "20px"}
                        )
                    ],
                    style={
                        "display": "flex",
                        "alignItems": "center",
                        "justifyContent": "flex-start",
                        "marginTop": "20px"
                    }
                ),

                html.Hr(
                    style={
                        "border": "1px solid #D3D3D3",
                        "marginTop": "20px",
                        "marginBottom": "20px"
                    }
                ),

                html.P(
                    "AF DETECT is a web-based platform designed to support clinical decision-making "
                    "in the field of atrial fibrillation, providing descriptive and predictive resources.",
                    className="text-left"
                ),

                html.H4("About", className="mt-4"),

                html.P(
                    "The platform was developed by Henrique Anjos, Rui Henriques, and Rafael Costa "
                    "at IST, in collaboration with ULSM.",
                    className="text-left"
                ),

                html.H4("Warnings", className="mt-4"),

                html.P(
                    "This tool is currently an in-development prototype intended for use in test "
                    "settings and should not be relied upon for definitive clinical decisions.",
                    className="text-left"
                ),

                html.Div(
                    html.Img(
                        src="/assets/ist_logo.png",
                        height="50px"
                    ),
                    className="d-flex justify-content-center",
                    style={"marginTop": "30px"}
                ),

            ])

        elif pathname == "/indice":

            return html.Div([

                html.H2("Risk Index", className="mt-4 mb-4"),

                dbc.Tabs([
                    dbc.Tab(label="Simple", tab_id="geral"),
                    dbc.Tab(label="Advanced", tab_id="comp"),
                    dbc.Tab(label="Multi-Label", tab_id="sever"),
                ], id="tabs", active_tab="geral"),

                html.Div(id="tab-content", className="mt-3"),
            ])

        elif pathname == "/ajuda":

            return html.H2("Coming Soon", className="mt-4")

        else:

            return html.H2("Page not found", className="mt-4")
