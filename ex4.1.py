graph={0:[1,2],1:[0,2],2:[0,1]}
nodes_user_choice = [0, 1, 2] #on veut vérifier si la séquence de noeuds 0 -> 1 -> 2 est une chaine 

def isChain(dic, nodes):
    for i in range(len(nodes)-1): #s'arreter à len(nodes)-1 car v2=i+1 donc il ne faut pas dépasser
        #len(nodes) vaut 3, donc i vaut 0,1,2
        
        v1 = nodes[i] #sommet de l'étape courante (par ex v1 = 0 pour l'étape 0->1)
        v2 = nodes[i+1] #sommet de d'arrivée de l'étape courante (par ex v2 = 1 pour l'étape 0->1)
        
        
        if v2 not in dic[v1]: #si 1 n'est pas dans la liste des voisins de 0, alors ce n'est pas une chaine
            return False
    
    return True #si on a parcouru toute la liste de noeuds sans rencontrer de problème, alors c'est une chaine


print(isChain(graph, nodes_user_choice))
