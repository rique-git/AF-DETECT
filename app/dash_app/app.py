import dash
from dash import html, dcc
import dash_bootstrap_components as dbc

from app.dash_app.components.navbar import navbar
from app.dash_app import callbacks


def create_dash_app():

    app = dash.Dash(
        __name__,
        external_stylesheets=[dbc.themes.FLATLY],
        suppress_callback_exceptions=True
    )

    app.layout = html.Div([
        dcc.Location(id='url', refresh=False),

        html.Div([
            navbar,
            dbc.Container(
                html.Div(id="page-content", className="flex-grow-1 mt-4")
            ),
        ], className="d-flex flex-column min-vh-100"),

        html.Footer(
            dbc.Container(
                html.Small([
                    "Copyright © 2025 | AF DETECT",
                    html.Br(),
                    "Updated: 2025-10-02"
                ], className="text-muted")
            ),
            className="text-center py-3 bg-light"
        )
    ])

    callbacks.display_page.register(app)
    callbacks.predict.register(app)
    callbacks.render_indice_risco.register(app)

    return app
