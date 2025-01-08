from dash import dcc, html

def create_histogramme_layout(data):
    continents = data['continent'].dropna().unique()
    return html.Div([
        html.H1("Histogramme par Décennie", style={"textAlign": "center"}),
        dcc.Dropdown(
            id="continent-dropdown",
            options=[{"label": continent, "value": continent} for continent in continents],
            placeholder="Choisissez un continent",
            style={"width": "50%", "margin": "auto"}
        ),
        dcc.Graph(id="histogram-graph")
    ])
