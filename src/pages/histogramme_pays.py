from dash import dcc, html

def create_histogramme_pays_layout(data):
    countries = data['country'].dropna().unique()
    return html.Div([
        html.H1("Histogramme par Pays", style={"textAlign": "center"}),
        dcc.Dropdown(
            id="country-dropdown",
            options=[{"label": country, "value": country} for country in countries],
            placeholder="Choisissez un ou plusieurs pays",
            multi=True,
            style={"width": "50%", "margin": "auto"}
        ),
        dcc.Graph(id="country-histogram-graph")
    ])
