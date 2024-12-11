import plotly.express as px
import pandas as pd

# Exemple de données avec le nom du pays, son code ISO et la population
data = {
    'Pays': ['France', 'United States', 'Germany', 'Japan', 'Brazil'],
    'Code ISO': ['FRA', 'USA', 'DEU', 'JPN', 'BRA'],
    'Population': [67391582, 331883986, 83883596, 125584838, 213993437]  # Population estimée
}

# Créer un DataFrame avec ces données
df = pd.DataFrame(data)

# Créer une carte choroplèthe en utilisant le code ISO des pays
fig = px.choropleth(df,
                    locations='Code ISO',  # Indiquer la colonne des codes ISO
                    color='Population',  # Indiquer la colonne pour la couleur
                    hover_name='Pays',  # Afficher le nom du pays quand on survole la carte
                    color_continuous_scale='Viridis',  # Choisir la palette de couleurs
                    title='Population des Pays')  # Titre de la carte

# Afficher la carte
fig.show()