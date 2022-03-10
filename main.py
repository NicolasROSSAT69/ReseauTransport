import time
from tkinter import *
from tkinter import ttk

def dijkstra(Gare, depart, arriver):
    assert all(Gare[u][v] >= 0 for u in Gare.keys() for v in Gare[u].keys())
    gare_precedente = {x: None for x in Gare.keys()}
    visited = {x: False for x in Gare.keys()}
    distance = {x: float('inf') for x in Gare.keys()}
    distance[depart] = 0
    not_visited = [(0, depart)]
    while not_visited:
        dNoeud, station_gare = not_visited.pop()
        if not visited[station_gare]:
            visited[station_gare] = True
            for children in Gare[station_gare].keys():
                dist_children = dNoeud + Gare[station_gare][children]
                if dist_children < distance[children]:
                    distance[children] = dist_children
                    gare_precedente[children] = station_gare
                    not_visited.append((dist_children, children))
        not_visited.sort(reverse=True)
    tempsTrajet = distance[arriver]
    trajet = calculer_trajet(depart, arriver, gare_precedente)
    return trajet, tempsTrajet


def calculer_trajet(depart, arriver, gare_precedente):
    trajet = [(arriver)]
    trajet.insert(0, gare_precedente[arriver])
    last = gare_precedente[arriver]

    while depart not in trajet:
        trajet.insert(0, gare_precedente[last])
        last = gare_precedente[last]
    return trajet


def parcours_profondeur(Gare, start, end):

    visited = []
    visited.append((start, [start]))

    while visited:
        (node, trajet) = visited.pop()
        adjacent_nodes = [n for n in Gare[node] if n not in trajet]
        for a in adjacent_nodes:
            if a == end:
                yield trajet + [a]
            else:
                visited.append((a, trajet + [a]))
    return trajet

def calculer_itinéraire(Gare):

    l = LabelFrame(fenetre, text="Resultats", padx=20, pady=20)
    l.pack(fill="both", expand="yes")

    depart = listeDepart.get()
    arrivee = listearrivee.get()

    # Calcul du trajet avec l'algo de dijkstra
    startDk = time.time()
    trajet, tempsTrajet = dijkstra(Gare, depart, arrivee)
    endDK = time.time()
    tpsDK = endDK - startDk

    #Affichage resulat parcours en profondeur
    Label(l, text="----------------------------------------------------------------------------------------------------------------------------").pack()
    Label(l, text="Resultat du calcul de l'itinéraire par un algo de Dijkstra : ", bg= "green", fg= "white").pack()

    Label(l, text=trajet).pack()
    Label(l, text="Temps du trajet : " + str(tempsTrajet) + "minutes").pack()

    Label(l, text="Le temps d'execution machine de l'algo de Dijkstra est de : (secondes) " + str(tpsDK)).pack()
    Label(l, text="Le résultat obtenu est le plus optimisé.").pack()
    Label(l, text="L'algo retourne l'itinéraire qu'il trouve pour aller du point de départ choisi au point d'arriver.").pack()
    Label(l, text="Cette itinéraire est calculer en prennant en compte le temps de trajet entre chaque gare").pack()
    Label(l, text="Le trajet ci-dessus est donc le plus rapide que l'on peut obtenir").pack()
    Label(l, text="----------------------------------------------------------------------------------------------------------------------------").pack()

    # Calcul du trajet avec l'algo de parcours en profondeur
    startPP = time.time()
    trajet = parcours_profondeur(Gare, depart, arrivee)
    endPP = time.time()
    tpsPP = endPP - startPP

    #Affichage resulat parcours en profondeur
    Label(l, text="----------------------------------------------------------------------------------------------------------------------------").pack()
    Label(l, text="Resultat du calcul de l'itinéraire par un algo de parcours en profondeur : ", bg= "orange", fg= "white").pack()

    compteur = 1
    for i in trajet:
        Label(l, text="Itinéraire" + str(compteur) + " : ", bg= "gray51", fg= "white").pack()
        Label(l, text=i).pack()
        compteur = compteur + 1

    Label(l, text="Le temps d'execution machine de l'algo de parcours en profondeur est de : (secondes) " + str(tpsPP)).pack()
    Label(l, text="Le résultat obtenu est loin d'être le plus optimisé.").pack()
    Label(l, text="L'algo retourne le premier itinéraire qu'il trouve pour aller du point de départ choisi au point d'arriver.").pack()
    Label(l, text="Ce n'est pas forcement le chemin le plus cours car il n'y a pas de gestion du temps de parcours").pack()
    Label(l, text="----------------------------------------------------------------------------------------------------------------------------").pack()
    Label(l, text="Pour relancer un calcul d'itinéraire veuillez relancer l'application", bg= "red", fg= "white").pack()


if __name__ == '__main__':

    # liste ajacence graphe
    Gare = {}
    Gare['Gare de Vaise'] = {'Valmy': 1}
    Gare['Valmy'] = {'Gare de Vaise': 1, 'Gorge de Loup': 1}
    Gare['Gorge de Loup'] = {'Valmy': 1, 'Vieux-Lyon': 1}
    Gare['Vieux-Lyon'] = {'Gorge de Loup': 1, 'Bellecour': 1}
    Gare['Bellecour'] = {'Vieux-Lyon': 1, 'Cordeliers': 1, 'Guillotière': 1, 'Ampère': 1}
    Gare['Guillotière'] = {'Bellecour': 1, 'Saxe Gambetta': 1}
    Gare['Saxe Gambetta'] = {'Guillotière': 1, 'Charpennes': 1}
    Gare['Cuire'] = {'Hénon': 1}
    Gare['Hénon'] = {'Cuire': 1, "Croix-Rousse": 1}
    Gare['Croix-Rousse'] = {'Hénon': 1, "Croix-Paquet": 1}
    Gare['Croix-Paquet'] = {'Croix-Rousse': 1, "Hôtel de Ville": 1}
    Gare['Hôtel de Ville'] = {'Croix-Paquet': 1, "Foch": 1, "Cordeliers": 1}
    Gare['Cordeliers'] = {'Hôtel de Ville': 1, "Bellecour": 1}
    Gare['Ampère'] = {'Bellecour': 1, "Perrache": 1}
    Gare['Perrache'] = {'Ampère': 1}
    Gare['Foch'] = {'Masséna': 1, "Hôtel de Ville": 1}
    Gare['Masséna'] = {'Foch': 1, "Charpennes": 1}
    Gare['Charpennes'] = {'Masséna': 1, "Saxe Gambetta": 1}

    fenetre = Tk()
    fenetre.title("Application Transport")

    # Création de la liste avec nom gare pour le combobox
    liste_combobox = ["Gare de Vaise", "Valmy", "Gorge de Loup", "Vieux-Lyon", "Bellecour", "Guillotière", "Saxe Gambetta", "Cuire", "Hénon", "Croix-Rousse", "Croix-Paquet", "Hôtel de Ville", "Cordeliers", "Ampère", "Perrache", "Foch", "Masséna", "Charpennes"]

    lDep = LabelFrame(fenetre, text="Point de départ", padx=20, pady=20)
    lDep.pack(fill="both", expand="yes")

    listeDepart = ttk.Combobox(lDep, values=liste_combobox)
    listeDepart.pack()
    listeDepart.current(0)

    lArv = LabelFrame(fenetre, text="Point d'arrivée", padx=20, pady=20)
    lArv.pack(fill="both", expand="yes")

    listearrivee = ttk.Combobox(lArv, values=liste_combobox)
    listearrivee.pack()
    listearrivee.current(4)

    l = LabelFrame(fenetre, text="Bouton de calcul de l'itinéraire", padx=20, pady=20)
    l.pack(fill="both", expand="yes")

    bouton = Button(l, text="Calculer", command=lambda: [calculer_itinéraire(Gare), l.destroy(), lDep.pack_forget(), lArv.pack_forget()])
    bouton.pack()



    fenetre.mainloop()
