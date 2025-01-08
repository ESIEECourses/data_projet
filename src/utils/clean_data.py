def clean_data(df):
    """
    Nettoie et prépare les données pour le tableau de bord.
    """
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

    continents_data.to_csv("data/cleaned/continents.csv", index=False)
    countries_data.to_csv("data/cleaned/countries.csv", index=False)

    return df
