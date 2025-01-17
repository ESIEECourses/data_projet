import dash_bootstrap_components as dbc
from dash import html

# Définition de la barre de navigation
navbar = dbc.NavbarSimple(
    [
        # Élément de navigation : Bouton d'information
        dbc.NavItem(
            dbc.NavLink(
                html.Img(
                    src="assets/github-mark-white.png",
                    alt="Source Code",
                    id="github-logo",
                ),
                href="https://github.com/ESIEECourses/data_projet",
                target="_blank",
                className="p-1",
            )
        ),
    ],
    brand="Dashboard",  # Nom de la marque ou titre affiché dans la barre
    id="navbar",  # Identifiant unique pour la barre de navigation (utile pour le style ou les interactions)
    color="dark",  # Couleur de fond de la barre de navigation
    dark=True,  # Active un thème sombre pour la barre
)
