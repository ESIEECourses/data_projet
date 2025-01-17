import dash
import pandas as pd
import dash_bootstrap_components as dbc
from dash import html, dcc, Input, Output
from src.pages.graph_co2 import co2_distribution_graph  # Importer la fonction pour créer le graphique de répartition de CO₂
from src.pages.map_co2 import co2_map  # Importer la fonction pour créer la carte des émissions de CO₂
from src.components.header import navbar  # Importer la barre de navigation
from src.components.filter import filters  # Importer les filtres pour la sélection
from src.utils.cleanData import clean_data  # Fonction pour nettoyer les données
from src.utils.getData import get_data  # Fonction pour récupérer les données brutes
from config import DATA_PATH

# Étape 1 : Récupérer les données brutes
get_data()

# Étape 2 : Nettoyer les données
clean_data()

# Charger les données dans un DataFrame Pandas
countries_data = pd.read_csv(DATA_PATH)

# Initialisation de l'application Dash avec le thème Bootstrap
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])


# Définition de la structure principale de l'application
app.layout = dbc.Container(
    [
        # Section 1 : Barre de navigation
        navbar,
        
        # Section 2 : Espacement sous la barre de navigation
        html.Div(className="mb-2"),
        
        # Section 3 : Filtres
        html.Div(filters, className="mb-4"),
        
        # Section 4 : Conteneur des graphiques
        dbc.Row(
            [
                # Colonne 1 : Graphique de répartition des émissions de CO₂
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Répartition des émissions de CO₂"),  # Titre de la carte
                            dbc.CardBody(
                                dcc.Graph(id="co2-distribution-graph")  # Graphique dynamique
                            ),
                        ],
                        className="mb-4"  # Marges externes
                    ),
                    sm=12,  # Taille pour les petits écrans (100%)
                    md=6    # Taille pour les écrans moyens et plus (50%)
                ),
                
                # Colonne 2 : Carte des émissions de CO₂ par habitant
                dbc.Col(
                    dbc.Card(
                        [
                            dbc.CardHeader("Carte des émissions de CO₂ par habitant"),  # Titre de la carte
                            dbc.CardBody(
                                dcc.Graph(id="co2-map")  # Graphique dynamique
                            ),
                        ],
                        className="mb-4"  # Marges externes
                    ),
                    sm=12,  # Taille pour les petits écrans (100%)
                    md=6    # Taille pour les écrans moyens et plus (50%)
                ),
            ],
            className="gx-4"  # Espacement horizontal entre les colonnes
        ),
    ],
    fluid=True  # Conteneur fluide pour s'adapter à différentes tailles d'écran
)

# Définition des callbacks pour mettre à jour les graphiques en fonction des filtres
@app.callback(
    [
        Output("co2-distribution-graph", "figure"),  # Sortie : graphique de répartition
        Output("co2-map", "figure")  # Sortie : carte des émissions
    ],
    Input("year-selector", "value")  # Entrée : année sélectionnée dans les filtres
)
def update_graphs(selected_year):
    """
    Met à jour les graphiques en fonction de l'année sélectionnée.
    
    Args:
        selected_year (int): Année sélectionnée par l'utilisateur via les filtres.
    
    Returns:
        tuple: Les figures des deux graphiques (répartition des émissions et carte).
    """
    # Générer le graphique de répartition des émissions de CO₂
    fig_co2_distribution = co2_distribution_graph(countries_data, selected_year)
    
    # Générer la carte des émissions de CO₂ par habitant
    fig_co2_map = co2_map(countries_data, selected_year)
    
    # Retourner les deux graphiques
    return fig_co2_distribution, fig_co2_map

# Lancement de l'application Dash
if __name__ == "__main__":
    app.run_server(debug=True)  # Démarre le serveur en mode debug
