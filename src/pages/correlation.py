from dash import dcc, html
import plotly.express as px

def create_histogramme(data):
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

# Callback pour mettre à jour l'histogramme en fonction du continent sélectionné
@app.callback(
    Output("histogram-graph", "figure"),
    Input("continent-dropdown", "value")
)
def update_histogram(selected_continent):
    filtered_data = data if selected_continent is None else data[data['continent'] == selected_continent]
    histogram = px.bar(
        filtered_data,
        x="decade",
        y="co2",
        title=f"Émissions de CO₂ par décennie ({selected_continent or 'Monde entier'})",
        labels={"decade": "Décennie", "co2": "Émissions de CO₂ (en millions de tonnes)"}
    )
    return histogram
