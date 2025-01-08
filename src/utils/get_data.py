import os
import pandas as pd
from clean_data import clean_data

base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
data_path = os.path.join(base_dir, "data", "raw", "owid-co2-data.csv")
cleaned_path = os.path.join(base_dir, "data", "cleaned", "cleaneddata.csv")

if not os.path.exists(data_path):
    raise FileNotFoundError(f"Le fichier source est introuvable : {data_path}")

df_raw = pd.read_csv(data_path)
df_cleaned = clean_data(df_raw)

os.makedirs(os.path.dirname(cleaned_path), exist_ok=True)
df_cleaned.to_csv(cleaned_path, index=False)

print(f"Données nettoyées et enregistrées dans {cleaned_path}")
