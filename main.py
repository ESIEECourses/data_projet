from dash import Dash, html, dcc, Input, Output
import os
import pandas as pd
import plotly.express as px
from src.utils.cleanData import clean_data
from src.pages.home import create_home_page
from src.pages.histogramme import create_histogramme_layout
from src.pages.carte import create_carte
from src.pages.histogramme_pays import create_histogramme_pays_layout

# Chemins des fichiers
raw_data_path = "data/raw/owid-co2-data.csv"
cleaned_data_path = "data/cleaned/"
cleaned_file = os.path.join(cleaned_data_path, "cleaneddata.csv")

# Effacer les données existantes si elles existent
if os.path.exists(cleaned_file):
    print(f"Suppression de l'ancien fichier : {cleaned_file}")
    os.remove(cleaned_file)

# Générer les nouvelles données nettoyées
os.makedirs(cleaned_data_path, exist_ok=True)
data = clean_data(raw_data_path, cleaned_data_path)

# Créer l'application
app = Dash(__name__, suppress_callback_exceptions=True)

# Définir le layout principal
app.layout = html.Div([
    dcc.Location(id="url"),
    html.Div(id="page-content")
])

# Routeur pour les pages
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/histogramme":
        return create_histogramme_layout(data)
    elif pathname == "/carte":
        return create_carte(data)
    elif pathname == "/histogramme_pays":
        return create_histogramme_pays_layout(data)
    else:
        return create_home_page()

# Callback pour mettre à jour l'histogramme
@app.callback(
    Output("histogram-graph", "figure"),
    Input("continent-dropdown", "value")
)
def update_histogram(selected_continent):
    filtered_data = data if selected_continent is None else data[data['continent'] == selected_continent]
    histogram = px.histogram(
        filtered_data,
        x="decade",
        y="co2",
        title=f"Émissions de CO₂ par décennie ({selected_continent or 'Monde entier'})",
        labels={"decade": "Décennie", "co2": "Émissions de CO₂ (en millions de tonnes)"}
    )
    return histogram

# Callback pour mettre à jour la carte
@app.callback(
    Output("map-graph", "figure"),
    Input("year-slider", "value")
)
def update_map(selected_year):
    filtered_data = data[data['year'] == selected_year]
    map_fig = px.choropleth(
        filtered_data,
        locations="iso_code",
        color="co2",
        hover_name="country",
        title=f"Émissions de CO₂ en {selected_year}",
        color_continuous_scale="Viridis"
    )
    return map_fig

# Callback pour mettre à jour l'histogramme par pays
@app.callback(
    Output("country-histogram-graph", "figure"),
    Input("country-dropdown", "value")
)
def update_histogram_pays(selected_countries):
    filtered_data = data if not selected_countries else data[data['country'].isin(selected_countries)]
    country_histogram = px.bar(
        filtered_data,
        x="year",
        y="co2",
        color="country",
        title="Émissions de CO₂ par pays",
        labels={"year": "Année", "co2": "Émissions de CO₂ (en millions de tonnes)"}
    )
    return country_histogram

if __name__ == "__main__":
    app.run_server(debug=True)
