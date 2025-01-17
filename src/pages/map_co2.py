import plotly.express as px
import pandas as pd

# Définir les couleurs globales pour les tranches de CO₂ par habitant
colors = {
    "0 à 1": "#577590",
    "1 à 3": "#43AA8B",
    "3 à 5": "#90BE6D",
    "5 à 7": "#F9C74F",
    "7 à 9": "#F8961E",
    "9 à 12": "#F3722C",
    "Plus de 12": "#F94144"
}

def co2_map(data, selected_year):
    """
    Génère une carte interactive représentant les émissions de CO₂ par habitant pour chaque pays 
    lors d'une année spécifique.

    Args:
        data (pd.DataFrame): Les données sources contenant les informations sur les émissions de CO₂.
        selected_year (int): L'année sélectionnée pour afficher les données.

    Returns:
        plotly.graph_objects.Figure: Une carte choroplèthe des émissions de CO₂ par habitant.
    """

    # Filtrer les données pour l'année sélectionnée
    filtered_data = data[data['year'] == selected_year].copy()

    # Appliquer des tranches (bins) aux valeurs d'émissions de CO₂ par habitant
    bins = [0, 1, 3, 5, 7, 9, 12, float('inf')]  # Définir les limites des tranches
    labels = ["0 à 1", "1 à 3", "3 à 5", "5 à 7", "7 à 9", "9 à 12", "Plus de 12"]  # Noms des tranches
    
    filtered_data["co2_per_personnes_tranches"] = pd.cut(
        filtered_data["co2_per_capita"],  # Colonne à découper
        bins=bins,  # Définir les bornes
        labels=labels,  # Définir les noms des catégories
        right=False  # Inclure la borne inférieure, exclure la borne supérieure
    )

    # Créer une carte choroplèthe avec Plotly Express
    fig = px.choropleth(
        filtered_data,  # Données filtrées
        locations="iso_code",  # Colonne contenant les codes ISO des pays
        hover_name="country",  # Colonne affichant le nom du pays au survol
        title=f"Carte des émissions de CO₂ par habitant par pays en tonnes par an ({selected_year})",
        labels={  # Labels pour les données affichées
            "iso_code": "Code ISO",
            "co2_per_capita": "CO₂ par habitant (en tonnes)",
            "co2": "Émissions totales de CO₂ (en million de tonnes)",
        },
        color="co2_per_personnes_tranches",  # Colonne utilisée pour la coloration
        color_discrete_map=colors,  # Définir les couleurs pour chaque tranche
        hover_data={  # Informations affichées au survol
            "co2_per_capita": True,  # Afficher les émissions par habitant
            "co2": True,  # Afficher les émissions totales
            "co2_per_personnes_tranches": False,  # Masquer les catégories dans l'infobulle
        },
    )

    return fig
