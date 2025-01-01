import pandas as pd

def clean_data(df):
    """
    Nettoie et prépare les données pour le tableau de bord.
    
    - Garde les colonnes nécessaires.
    - Supprime les lignes avec des valeurs manquantes pour les colonnes critiques.
    - Ajoute une colonne 'decade' regroupant les années par décennie.
    
    Args:
        df (pd.DataFrame): Les données brutes.
    
    Returns:
        pd.DataFrame: Les données nettoyées et enrichies.
    """
    # Colonnes à conserver
    cols_to_keep = [
        "country", "year", "iso_code", "co2", "co2_per_capita", 
        "co2_per_gdp", "co2_including_luc", "cement_co2", "coal_co2", 
        "gas_co2", "oil_co2", "primary_energy_consumption", 
        "energy_per_capita", "share_global_co2"
    ]
    # Garder uniquement ces colonnes
    df = df[cols_to_keep]
    
    # Supprimer les lignes avec des valeurs manquantes critiques
    df = df.dropna(subset=["co2", "country", "year"])
    
    # Créer une colonne pour les décennies
    df["decade"] = (df["year"] // 10) * 10
    df["decade"] = df["decade"].astype(str) + "s"

    # Identifier les continents et les pays sans ISO code
    continents_list = ["Asia", "Europe", "North America", "South America", "Africa", "Oceania", "Antarctica"]
    continents_data = data[data['country'].isin(continents_list)]
    countries_data = data.dropna(subset=['iso_code'])  # Supprimer les pays sans ISO code

    # Sauvegarder les fichiers séparés
    continents_data.to_csv("data/cleaned/continents.csv", index=False)
    countries_data.to_csv("data/cleaned/countries.csv", index=False)
    
    # Retourner le DataFrame nettoyé
    return df