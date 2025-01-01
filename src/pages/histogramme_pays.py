from dash import dcc, html
import plotly.express as px

def create_histogramme_pays(data):
    countries = data['country'].dropna().unique()  # Obtenir les pays uniques

    return html.Div([
        html.H1("Histogramme par pays"),
        dcc.Dropdown(
            id="country-dropdown",
            options=[{"label": country, "value": country} for country in countries],
            placeholder="Choisissez un pays",
            multi=True  # Permet de sélectionner plusieurs pays
        ),
        dcc.Graph(id="country-histogram-graph")
    ])

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
