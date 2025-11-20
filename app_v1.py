from dash import html, dcc
import dash_bootstrap_components as dbc

from components.navbar import navbar
import callbacks

from myapp import app



app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    
    html.Div([
        navbar,
        dbc.Container(  # ← This keeps your content centered
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
    


if __name__ == '__main__':
    app.run(debug=True, port=8051)
