import pandas as pd

def clean_data(input_path, output_path):
    """
    Nettoie et prépare les données pour le tableau de bord.

    Args:
        input_path (str): Chemin vers les données brutes.
        output_path (str): Chemin pour sauvegarder les données nettoyées.
    """
    df = pd.read_csv(input_path)

    cols_to_keep = [
        "country", "year", "iso_code", "co2", "co2_per_capita",
        "co2_per_gdp", "co2_including_luc", "cement_co2", "coal_co2",
        "gas_co2", "oil_co2", "primary_energy_consumption",
        "energy_per_capita", "share_global_co2"
    ]
    df = df[cols_to_keep]
    df = df.dropna(subset=["co2", "country", "year"])

    df["decade"] = (df["year"] // 10) * 10
    df["decade"] = df["decade"].astype(str) + "s"

    continents_list = ["Asia", "Europe", "North America", "South America", "Africa", "Oceania", "Antarctica"]
    continents_data = df[df['country'].isin(continents_list)]
    countries_data = df.dropna(subset=["iso_code"])

    continents_data.to_csv(output_path + "continents.csv", index=False)
    countries_data.to_csv(output_path + "countries.csv", index=False)

    df.to_csv(output_path + "cleaneddata.csv", index=False)
    return df
