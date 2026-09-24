def estVoisin(v1, v2, dic):
    """
    Cette fonction prend en entrée deux sommets v1 et v2 ainsi qu'un dictionnaire dic représentant un graphe.
    Elle retourne True si v2 est un voisin de v1 dans le graphe, sinon elle retourne False.
    """
    return v2 in dic[v1]

def estVoisin(v1, v2, mat):
    """
    Cette fonction prend en entrée deux sommets v1 et v2 ainsi qu'une matrice d'adjacence mat représentant un graphe.
    Elle retourne True si v2 est un voisin de v1 dans le graphe, sinon elle retourne False.
    """
    return mat[v1][v2] == 1

def estChaine(dic, list_nodes):
    """
    Cette fonction prend en entrée un dictionnaire dic représentant un graphe et une liste de sommets list_nodes.
    Elle retourne True si la liste de sommets forme une chaîne dans le graphe, sinon elle retourne False.
    """
    for i in range(len(list_nodes) - 1):
        if estVoisin(list_nodes[i], list_nodes[i + 1], dic) == False:
            return False
    return True

def estChaineElementaire(dic, list_nodes):
    
    if not estChaine(dic, list_nodes):
        return False

    return len(list_nodes) == len(set(list_nodes))  # Vérifie si tous les sommets sont distincts

def isSimpleChain(dic, list_nodes):
    lg = len(list_nodes)
    aretes = []
    for i in range(lg - 1):
        v1 = list_nodes[i]
        v2 = list_nodes[i + 1]
        if (v1, v2) in aretes or (v2, v1) in aretes:
            return False
        aretes.append((v1, v2))
    return True 


def isGraphFull(dic):
    n = len(dic)
    for node in dic: #pour chaque noeud du graphe, on verifie si le nombre de voisins est égal à n-1 (car un noeud ne peut pas etre voisin de lui meme)
        if len(dic[node]) != n-1: # si le nombre de voisins d'un noeud est different de n-1, alors le graphe n'est pas complet
            return False
    return True


def isGraphFull2(dic):
    n = len(dic)
    for i in dic.keys(): 
        if not len(dic[i]) == n-1: 
            return False
    return True



def degre(dic, v):
    return len(dic[v])

def isFull(dic):
    nbNodes = len(dic)
    for node in range(nbNodes):
        if len(dic[node]) != nbNodes-1:
            return False
    return True

def 
    
def isGraphBipartite(dic)