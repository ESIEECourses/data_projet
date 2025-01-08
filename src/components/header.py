from dash import html, dcc

def header():
    """
    Crée un en-tête pour le tableau de bord avec des liens vers les pages principales.
    """
    return html.Header(
        style={
            "display": "flex",
            "justifyContent": "space-between",
            "alignItems": "center",
            "padding": "1em",
            "backgroundColor": "#007BFF",
            "color": "white"
        },
        children=[
            html.H1("Mon Dashboard", style={"margin": "0", "fontSize": "1.5em"}),
            html.Nav(
                style={"display": "flex", "gap": "1em"},
                children=[
                    dcc.Link("Dashboard", href="/", style={"color": "white", "textDecoration": "none"}),
                    dcc.Link("Histogramme", href="/histogramme", style={"color": "white", "textDecoration": "none"}),
                    dcc.Link("Carte", href="/carte", style={"color": "white", "textDecoration": "none"})
                ]
            )
        ]
    )
