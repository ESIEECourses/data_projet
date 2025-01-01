import sys
import os
import pandas as pd
from dash import Dash, dcc, html  # Import cohérent
from dash.dependencies import Input, Output

# Ajoute le dossier source au chemin d'import
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.append(src_path)

# Maintenant, les imports fonctionnent
from pages.home import create_home_page
from pages.histogramme import create_histogramme
from pages.carte import create_carte

# Charger les données nettoyées
data = pd.read_csv("data/cleaned/cleaneddata.csv")

# Création de l'application Dash
app = Dash(__name__)

# Définition du layout principal
app.layout = html.Div([
    dcc.Location(id="url"),  # Permet de gérer les URLs
    html.Div(id="page-content")  # Contenu de la page dynamique
])

# Router pour changer de page
@app.callback(
    Output("page-content", "children"),
    Input("url", "pathname")
)
def display_page(pathname):
    if pathname == "/histogramme":
        return create_histogramme(data)  # Remplace simple_page
    elif pathname == "/carte":
        return create_carte(data)  # Remplace complex_page
    else:
        return create_home_page()  # Page d'accueil

# Exécuter le serveur
if __name__ == "__main__":
    app.run_server(debug=True)
