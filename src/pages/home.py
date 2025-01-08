from dash import html, dcc

def create_home_page():
    return html.Div(
        style={"padding": "20px"},
        children=[
            html.H1("Global CO₂ Dashboard", style={"textAlign": "center"}),
            html.P(
                """
                Bienvenue dans le tableau de bord interactif sur les émissions de CO₂. 
                Explorez les données liées aux émissions de dioxyde de carbone et aux indicateurs environnementaux.
                """,
                style={"textAlign": "center"}
            ),
            html.Div(
                style={"textAlign": "center", "marginTop": "20px"},
                children=[
                    dcc.Link("Histogramme", href="/histogramme", style={"marginRight": "20px"}),
                    dcc.Link("Carte", href="/carte", style={"marginRight": "20px"}),
                    dcc.Link("Histogramme par Pays", href="/histogramme_pays")
                ]
            )
        ]
    )
