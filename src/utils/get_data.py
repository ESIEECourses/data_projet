import os
import pandas as pd
from clean_data import clean_data

# Construire le chemin relatif
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Le répertoire 'src'
data_path = os.path.join(base_dir, "..", "data", "raw", "owid-co2-data.csv")

# Charger les données brutes
df_raw = pd.read_csv(data_path)

# Appliquer le nettoyage
df_cleaned = clean_data(df_raw)

# Sauvegarder les données nettoyées
df_cleaned.to_csv("data/cleaned/cleaneddata.csv", index=False)

print("Données nettoyées et enregistrées dans data/cleaned/cleaneddata.csv")