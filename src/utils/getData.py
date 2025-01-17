import os
import requests

def get_data():
    """
    Télécharge un fichier depuis une URL et le sauvegarde à l'emplacement spécifié.
    Écrase tout fichier existant sous le même nom.

    Returns:
        None
    """
    # URL du fichier à télécharger
    url = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
    
    # Chemin de sauvegarde du fichier, y compris le nom du fichier
    save_path = "data/raw/raw.csv"

    try:
        # Création des répertoires nécessaires (si inexistants)
        os.makedirs(os.path.dirname(save_path), exist_ok=True)
        
        # Envoi d'une requête GET pour télécharger le fichier
        response = requests.get(url)
        response.raise_for_status()  # Vérifie s'il y a des erreurs HTTP (exemple : 404, 500)
        
        # Sauvegarde du contenu téléchargé dans un fichier local
        with open(save_path, 'wb') as file:
            file.write(response.content)  # Écriture du contenu brut dans le fichier
        
        # Confirmation du succès
        print(f"Fichier téléchargé et sauvegardé à : {save_path}")
    
    # Gestion des erreurs liées à la requête HTTP
    except requests.exceptions.RequestException as e:
        print(f"Erreur lors du téléchargement : {e}")
    
    # Gestion des erreurs générales (par exemple, problème lors de l'écriture du fichier)
    except Exception as e:
        print(f"Erreur lors de la sauvegarde du fichier : {e}")
