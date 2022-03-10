
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

    depart = 'Gare de Vaise'
    arriver = 'Charpennes'

    #Calcul du trajet avec l'algo de dijkstra
    print("Itinéraire calculé avec l'algo de Dijkstra : ")
    trajet, tempsTrajet = dijkstra(Gare, depart, arriver)
    print(trajet)
    print("Temps du trajet :", tempsTrajet, "minutes \n")

    #Calcul du trajet avec l'algo de parcours en profondeur
    print("Itinéraire calculé avec l'algo de parcours en profondeur : ")
    trajet = parcours_profondeur(Gare, depart, arriver)
    for i in trajet:
        print(i)
    #for i in range(len(trajet)):
        #print(trajet[i])


