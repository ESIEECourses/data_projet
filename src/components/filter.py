import dash_bootstrap_components as dbc
from dash import dcc, html

filters = dbc.Row(
    dbc.Col(
        dbc.Card(
            [
                dbc.CardHeader(
                    [
                        dbc.Button(
                            [
                                html.P("Filters", className="m-0"),
                            ],
                            id="filter-header-btn",
                            className="w-100 p-3 d-flex justify-content-between",
                            color="light",
                            n_clicks=0,
                        ),
                    ],
                    className="p-0 m-0",
                ),
                dbc.Collapse(
                    dbc.CardBody(
                        [
                            dbc.Row(
                                dbc.Col(
                                    dcc.Dropdown(
                                        id="year-selector",
                                        options=[{"label": str(year), "value": year} for year in range(1850, 2024)],
                                        value=2023,  # Valeur par défaut
                                        placeholder="Choisissez une année",
                                        clearable=True
                                    )
                                )
                            )
                        ]
                    ),
                    id="filter-collapse",
                    is_open=True
                ),
            ]
        )
    ),
    id="filters",
)
