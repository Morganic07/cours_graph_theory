# --- 1. AJOUTER UNE ROUTE ---
def add_edge(graph, u, v, w):
    # 'graph' est une liste. On y dépose un nouveau paquet : [ville_A, ville_B, prix].
    # En mémoire : on agrandit simplement la liste avec un nouvel élément à la fin.
    graph.append([u, v, w])


def find_parent(parent, i):
    # Condition d'arrêt (point fixe) :
    # Un sommet 'i' est la racine de sa composante connexe si et seulement si
    # la table de routage indique qu'il pointe vers lui-même (parent[i] == i).
    if parent[i] == i:
        return i
    
    # Étape de descente (ou plutôt de remontée dans l'arborescence) :
    # Si 'i' n'est pas une racine, parent[i] contient l'identifiant de son ascendant direct.
    # On empile un nouvel appel récursif sur parent[i] pour continuer la traversée. 
    # Complexité pire cas : O(h), où h est la hauteur de la branche (dégénérescence possible en O(V)).
    return find_parent(parent, parent[i])

# --- 3. FUSIONNER DEUX GROUPES ---
def union(parent, rank, x, y):
    # On cherche les deux chefs suprêmes des éléments x et y.
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    # Pour éviter d'avoir de trop longues chaînes (ce qui ralentirait les recherches),
    # on regarde la hauteur (le 'rank') des deux groupes :
    
    # Cas 1 : le groupe de Y est plus profond que celui de X.
    # On rattache le chef de X sous le chef de Y.
    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
        
    # Cas 2 : le groupe de X est plus profond que celui de Y.
    # On rattache le chef de Y sous le chef de X.
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
        
    # Cas 3 : les deux groupes ont exactement la même hauteur.
    # On choisit arbitrairement de mettre Y sous X, et comme la pyramide
    # prend un niveau de plus, on augmente le rang de X de 1.
    else:
        parent[yroot] = xroot
        rank[xroot] += 1


# --- 4. ALGORITHME DE KRUSKAL ---
def kruskal(graph, V):
    # Liste finale des routes retenues.
    result = []
    
    # 'i' : indice pour parcourir les routes de la liste triée (route 0, puis route 1...).
    i = 0
    # 'e' : compteur du nombre d'arêtes déjà acceptées dans le réseau final.
    e = 0

    # ÉTAPE 1 : Tri glouton.
    # 'lambda item: item[2]' signifie : "regarde l'élément à l'index 2 (le coût 'w')".
    # On classe les routes de la moins chère à la plus chère.
    graph = sorted(graph, key=lambda item: item[2])

    # ÉTAPE 2 : Initialisation de la mémoire.
    # Au départ, chaque ville est isolée : elle est son propre parent.
    # Exemple pour 4 villes : parent devient [0, 1, 2, 3].
    parent = [i for i in range(V)]
    
    # Au départ, chaque groupe a une hauteur de 0.
    rank = [0] * V

    # ÉTAPE 3 : Sélection des routes.
    # Règle d'or : pour relier V sommets sans boucle, il faut exactement (V - 1) arêtes.
    while e < V - 1:
        # On extrait la prochaine route la moins chère.
        u, v, w = graph[i]
        i = i + 1

        # On cherche à quels groupes appartiennent 'u' et 'v'.
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        # TEST ANTI-CYCLE :
        # Si x et y sont différents, les deux villes ne sont pas encore connectées.
        # Cette route est donc sûre (elle ne crée pas de boucle fermée).
        if x != y:
            e = e + 1
            result.append([u, v, w]) # On garde cette route.
            union(parent, rank, x, y) # On fusionne leurs deux groupes.

    # On retourne le réseau optimal.
    return result