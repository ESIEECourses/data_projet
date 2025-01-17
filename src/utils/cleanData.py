import os
import pandas as pd

def clean_data():
    """
    Nettoie et prépare les données pour le tableau de bord.
    Cette fonction effectue les étapes suivantes :
    - Supprime tous les fichiers existants dans le répertoire `cleaned`.
    - Charge les données brutes depuis un fichier CSV.
    - Nettoie les colonnes nécessaires et les types de données.
    - Ajoute une colonne représentant la décennie.
    - Sépare les données en deux fichiers : pays et continents.
    - Sauvegarde les fichiers nettoyés dans un répertoire dédié.

    Returns:
        pd.DataFrame: Le DataFrame complet contenant les données nettoyées.
    """

    # Chemin d'entrée des données brutes
    input_path = "data/raw/raw.csv"

    # Répertoire pour les données nettoyées
    output_path = "data/cleaned"

    # Étape 1 : Supprimer les fichiers existants dans le répertoire `cleaned`
    if os.path.exists(output_path):
        for file in os.listdir(output_path):
            file_path = os.path.join(output_path, file)
            if os.path.isfile(file_path):
                os.remove(file_path)  # Suppression du fichier
    else:
        os.makedirs(output_path)  # Création du répertoire s'il n'existe pas

    # Étape 2 : Charger les données depuis le fichier CSV
    # Définir les types des colonnes pour éviter les erreurs de chargement
    df = pd.read_csv(input_path, dtype={
        'co2': float,
        'co2_per_capita': float,
        'co2_per_gdp': float,
        'co2_including_luc': float,
        'cement_co2': float,
        'coal_co2': float,
        'gas_co2': float,
        'oil_co2': float,
        'primary_energy_consumption': float,
        'energy_per_capita': float,
        'share_global_co2': float
    })

    # Étape 3 : Sélection des colonnes nécessaires
    cols_to_keep = [
        "country", "year", "iso_code", "co2", "co2_per_capita","co2_growth_abs"
    ]
    
    # Vérifier que toutes les colonnes nécessaires sont présentes
    missing_cols = [col for col in cols_to_keep if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Les colonnes suivantes sont manquantes dans le fichier d'entrée : {missing_cols}")

    df = df[cols_to_keep]

    # Étape 4 : Nettoyage des colonnes numériques
    numeric_columns = ["co2", "co2_per_capita", "co2_growth_abs"]
    for col in numeric_columns:
        if col in df.columns:
            # Convertir en chaîne pour manipulation et remplacer les virgules par des points
            df[col] = (
                df[col]
                .astype(str)
                .str.replace(",", ".", regex=False)  # Remplacer les virgules par des points
            )
            # Convertir en float après le remplacement
            df[col] = pd.to_numeric(df[col], errors='coerce')

    # Étape 5 : Supprimer les lignes avec des valeurs manquantes dans des colonnes critiques
    df = df.dropna(subset=["co2", "country", "year"])

    # Étape 6 : Ajouter une colonne pour la décennie
    df["decade"] = (df["year"] // 10) * 10  # Calcul de la décennie
    df["decade"] = df["decade"].astype(str) + "s"  # Formatage en chaîne

    # Étape 7 : Séparer les données pour les pays et les continents
    continents = ["Asia", "Europe", "North America", "South America", "Africa", "Oceania", "Antarctica"]
    continents_data = df[df["country"].isin(continents) & df["iso_code"].isna()]  # Données des continents
    countries_data = df[df["iso_code"].notna()]  # Données des pays

    # Étape 8 : Sauvegarder les fichiers nettoyés
    countries_data.to_csv(f"{output_path}/countries.csv", index=False)
    continents_data.to_csv(f"{output_path}/continents.csv", index=False)
    df.to_csv(f"{output_path}/cleaneddata.csv", index=False)

    # Afficher les chemins des fichiers sauvegardés
    print(f"Données nettoyées et sauvegardées dans : {output_path}")
    print(f"- Fichier pour les pays : {output_path}/countries.csv")
    print(f"- Fichier pour les continents : {output_path}/continents.csv")
    print(f"- Données complètes nettoyées : {output_path}/cleaneddata.csv")

    # Retourner le DataFrame nettoyé
    return df
