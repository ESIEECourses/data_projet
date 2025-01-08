from dash import dcc, html

def create_carte(data):
    years = sorted(data['year'].unique())
    return html.Div([
        html.H1("Carte des Émissions de CO₂", style={"textAlign": "center"}),
        dcc.Slider(
            id="year-slider",
            min=min(years),
            max=max(years),
            marks={year: str(year) for year in years[::10]},
            step=1,
            value=min(years),
            tooltip={"placement": "bottom", "always_visible": True},
        ),
        dcc.Graph(id="map-graph")
    ])
