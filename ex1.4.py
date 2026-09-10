graph={0:[1,2],1:[0,2],2:[0,1]}

#Each key represent a node, its value is the list of its neighbors

def showStruct(dic):
    print("Nodes :")
    for node in dic.keys(): #dic.keys() donne la liste des clés de dic, donc la liste des noeuds
        print("v"+str(node),end=" ")
    print("")    
    print("Edges :")
    for node in dic.keys():
        for neighbor in dic[node]:
            if (node < neighbor):
                print("v"+str(node)+"--- v"+str(neighbor))
showStruct(graph)    
