import os
import pandas as pd
from utils.cleanData import clean_data

# Construire le chemin relatif
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))  # Le répertoire 'src'
data_path = os.path.join(base_dir, "..", "data", "raw", "owid-co2-data.csv")

# Charger les données brutes
df_raw = pd.read_csv(data_path)

# Appliquer le nettoyage
df_cleaned = clean_data(df_raw)

# Vérifier le résultat
print(df_cleaned.head())
print(df_cleaned["decade"].unique())  # Vérifie les décennies
