from dash import html, Input, Output
import dash_bootstrap_components as dbc

from myapp import app

@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/inicio" or pathname == "/":
        return html.Div([

            # Welcome text + Logo side by side
            html.Div(
                [
                    html.H1("Welcome to", className="mb-0"),
                    html.Img(src="/assets/logo.png", height="80px", style={"marginLeft": "20px"})
                ],
                style={"display": "flex", "alignItems": "center", "justifyContent": "flex-start", "marginTop": "20px"}
            ),

            # Slim grey separator
            html.Hr(style={"border": "1px solid #D3D3D3", "marginTop": "20px", "marginBottom": "20px"}),

            # Platform Description
            html.P("AF DETECT is a web-based platform designed to support clinical decision-making in " \
                    "the field of atrial fibrillation, providing descriptive and predictive resources. ", className="text-left"),

            # About the platform
            html.H4("About", className="mt-4"),
            html.P("The platform was developed by Henrique Anjos, Rui Henriques, and Rafael Costa at IST, in collaboration with ULSM.", className="text-left"),

            # Disclaimer
            html.H4("Warnings", className="mt-4"),
            html.P("This tool is currently an in-development prototype intended for use in test settings and should not be relied " \
            "upon for definitive clinical decisions. The authors cannot guarantee the accuracy of the calculations for any individual patient.", className="text-left"),

            # IST Logo at the bottom
            html.Div(
                html.Img(src="/assets/ist_logo.png", height="50px"),  # Adjust image source and size
                className="d-flex justify-content-center",
                style={"marginTop": "30px"}
            ),
            
        ])  # your inicio content
    
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