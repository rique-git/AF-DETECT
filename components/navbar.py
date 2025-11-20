import dash_bootstrap_components as dbc
from dash import html

navbar = dbc.Navbar(
    dbc.Container([
        # Left: Logo or App Name
        html.A(
            dbc.Row([
                dbc.Col(html.Img(src="/assets/logo.png", height="30px")),  # You can put your logo in /assets
            ], align="center", className="g-0"),
            href="#",
            style={"textDecoration": "none"}
        ),

        # Center: Navigation items
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("Home", href="/inicio")),
            dbc.NavItem(dbc.NavLink("Risk Index", href="/indice")),
            dbc.NavItem(dbc.NavLink("FAQs", href="/ajuda")),
        ], className="mx-auto", navbar=True),

        # Right: Language or login (optional)
        dbc.Nav([
            dbc.NavItem(dbc.NavLink("PT", href="#")),
        ], navbar=True),
    ]),
    color="#276f48",
    dark=True,
    sticky="top",
)