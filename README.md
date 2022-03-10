# ReseauTransport
Projet algo M1 AL

## Sujet
Vous construirez un graphe représentant un réseau de transport existant constitué d’environ 10 à 20 destinations, présentant une structure de type graphe (avec au moins un cycle). 
Vous créerez un outil permettant à un utilisateur de choisir un point de départ, un point d’arrivé et de lui indiquer l’itinéraire à suivre. Cet itinéraire sera calculé via au moins 2 manières différentes. 
Vous comparerez les résultats en temps de transport prévu pour l’utilisateur de ces différentes méthodes et présenterez la complexité en temps que ces algorithmes ont engendrés dans leur calcul.

## Documentations

La documentation du projet est dans le fichier documentation.pdf
Vous y trouverez le plan du réseau de transport utilisé ainsi que la matrice d'adjacence.
Les algos calculent un itinéraire à partir d'une liste d'adjacence (dict en python)

## Version 
Python 3.9
PyCharm (JetBrains)
Tkinter

## Conclusion
L'algo de dijkstra est un peu plus long à executer que l'algo de parcours en profondeur mais il est plus précis car il prend en compte la durée de trajet entre les diférentes gare de métro (Branch, node).
Et ressort le trajet le plus court pour aller du point A au point B.
L'algo de parcours en profondeur ressort quand à lui les différents itinéraires possibles pour se rendre entre le point A et B, sans prendre en compte le temps de transport.
Comme dans mon exemple la matrice d'adjacence à uniquement des valeur 0 et 1, le temps pour aller de gare en gare est de 1 minutes mais d'autres valeurs aurait pu s'y trouver.