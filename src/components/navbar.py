from dash import html

(TODO)
def navbar():
    return html.Nav([
        html.A("Accueil", href="/", style={"marginRight": "10px"}),
        html.A("À propos", href="/about")
    ], style={"padding": "1em", "backgroundColor": "#ccc"})
