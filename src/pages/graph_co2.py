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

def co2_distribution_graph(data, selected_year):
    """
    Génère un graphique à barres représentant la répartition des pays 
    en fonction des tranches d'émissions de CO₂ par habitant pour une année donnée.

    Args:
        data (pd.DataFrame): Les données sources contenant les informations sur les émissions de CO₂.
        selected_year (int): L'année sélectionnée pour afficher les données.

    Returns:
        plotly.graph_objects.Figure: Un graphique à barres montrant la répartition des pays.
    """

    # Filtrer les données pour l'année sélectionnée
    filtered_data = data[data['year'] == selected_year].copy()
    
    # Définir les tranches (bins) et leurs labels
    bins = [0, 1, 3, 5, 7, 9, 12, float('inf')]  # Limites des tranches
    labels = ["0 à 1", "1 à 3", "3 à 5", "5 à 7", "7 à 9", "9 à 12", "Plus de 12"]  # Noms des tranches

    # Créer une nouvelle colonne pour catégoriser les pays en fonction des tranches de CO₂ par habitant
    filtered_data.loc[:, "co2_per_capita_bins"] = pd.cut(
        filtered_data["co2_per_capita"],  # Colonne à découper
        bins=bins,  # Définir les bornes
        labels=labels,  # Définir les noms des catégories
        right=False  # Inclure la borne inférieure, exclure la borne supérieure
    )

    # Grouper les données par tranches et compter le nombre de pays dans chaque tranche
    grouped_data = filtered_data.groupby(
        ['co2_per_capita_bins'],  # Grouper par tranches de CO₂
        observed=True  # Inclure uniquement les tranches présentes dans les données
    ).size().reset_index(name="Number of Countries")  # Ajouter une colonne avec le nombre de pays

    # Créer un graphique à barres avec Plotly Express
    fig = px.bar(
        grouped_data,  # Données regroupées
        x="co2_per_capita_bins",  # Axe des X : tranches de CO₂ par habitant
        y="Number of Countries",  # Axe des Y : nombre de pays
        title=f"Répartition des pays par tranche de CO₂ par habitant en tonnes par an ({selected_year})",
        labels={  # Personnalisation des étiquettes
            "co2_per_capita_bins": "CO₂ par habitant en tonnes",
            "Number of Countries": "Nombre de pays"
        },
        color="co2_per_capita_bins",  # Coloration des barres par tranches
        color_discrete_map=colors,  # Appliquer les couleurs définies pour chaque tranche
        barmode="stack"  # Mode empilé (optionnel, ici chaque barre représente une catégorie)
    )

    return fig
