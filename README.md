# data_projet
 Projet en python

## Auteurs
- [@Aissatou28](https://github.com/Aissatou28)
- [@assiamxn](https://github.com/assiamxn)

## Guide

## Data
Les [données utilisées](https://github.com/owid/co2-data?tab=readme-ov-file) sont fournis par [Our World In Data](https://ourworldindata.org/) et sont récupérée dynamiquement.
Le set de data provient de plusieurs sources que vous pouvez trouver directement dans le readme.  

## Developer guide
data_project
|-- .venv
|   |-- *
|-- assets                                       # les données
│   |-- figure_descriptions.json
│   |-- github-mark-white.png
│   |-- styles.css
|-- 𝗱𝗮𝘁𝗮                                        # les données
│   |-- cleaned
│   │   |-- cleaneddata.csv                     # ensembles des pays/contients/groupes
│   │   |-- continents.csv                      # continents
│   │   |-- countries.csv                       # pays
│   |-- 𝗿𝗮𝘄
│       |-- raw.csv                 
|-- 𝘀𝗿𝗰                                          # le code source du dashboard
|   |-- components                              # les composants du dashboard
|   |   |-- __init__.py
|   |   |-- filter.py
|   |   |-- header.py
|   |   |-- MetricCard.py
|   |-- pages                                   # les pages du dashboard
|   |   |-- __init__.py
|   |   |-- graph_co2.py
|   |   |-- map_co2.py
|   |-- 𝘂𝘁𝗶𝗹𝘀                                    # les fonctions utilitaires
|   |   |-- __init__.py
|   |   |-- clean_data.py                       # script de nettoyage des données
|   |   |-- get_data.py                         # script de récupération des données
|-- gitignore 
|-- 𝗰𝗼𝗻𝗳𝗶𝗴.𝗽𝘆                                    # fichier de configuration
|-- 𝗺𝗮𝗶𝗻.𝗽𝘆                                     # fichier principal permettant de lancer le dashboard
|-- 𝗥𝗘𝗔𝗗𝗠𝗘.𝗺𝗱
|-- 𝗿𝗲𝗾𝘂𝗶𝗿𝗲𝗺𝗲𝗻𝘁𝘀.𝘁𝘅𝘁                              # liste des packages additionnels requis
|-- demo.mov                                     # demonstration du dashboard

## Rapport d'analyse
On peut voir dans les statisiques générales que les pays les plus émetteurs de co2 ne sont pas forcément ceux dont les habitants en produisent le plus. Et qu'il y a une légère baisse générale quant à l'émissions de co2 par personne au cours des dernières années.

## Copyritght
Nous déclarons sur honneur que le code fourni a été produit par nous même, à l’exception deux fichiers ci dessous:
* /src/components/MetricCard.py
* /src/components/header.py
Qui sont basé sur le code de [Jwolf](https://stream-metrics-b5f68d63e431.herokuapp.com/).
Ils ont été utilsée afin d'améliorer l'aspect visuel du code.


## Ressources
Hannah Ritchie, Pablo Rosado and Max Roser (2023) - “CO₂ and Greenhouse Gas Emissions” Published online at OurWorldinData.org.
Retrieved from: 'https://ourworldindata.org/co2-and-greenhouse-gas-emissions' [Online Resource]