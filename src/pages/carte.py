from dash import dcc, html
import plotly.express as px

def create_carte(data):
    years = sorted(data['year'].unique())  # Liste des années

    return html.Div([
        html.H1("Carte des émissions de CO₂"),
        dcc.Slider(
            id="year-slider",
            min=min(years),
            max=max(years),
            marks={year: str(year) for year in years[::10]},  # Une marque tous les 10 ans
            step=1,
            value=min(years)  # Année initiale
        ),
        dcc.Graph(id="map-graph")
    ])

# Callback pour mettre à jour la carte en fonction de l'année sélectionnée
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
        color_continuous_scale="Viridis"  # Tu peux changer la palette ici
    )
    return map_fig
