from dash import Dash, dcc, html, Input, Output
import plotly.express as px

def create_histogramme(data,app):
    continents = data['continent'].dropna().unique()  # Obtenir les continents uniques

    return html.Div([
        html.H1("Histogramme par décennie"),
        dcc.Dropdown(
            id="continent-dropdown",
            options=[{"label": continent, "value": continent} for continent in continents],
            placeholder="Choisissez un continent",
        ),
        dcc.Graph(id="histogram-graph")
    ])