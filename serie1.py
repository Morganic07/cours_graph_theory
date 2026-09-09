#exercice 1.3


graph = [[0, 1, 1], [1, 0, 1], [1, 1, 0]]

def showStruct(mat):
    nbNodes = len(mat)
    print("Number of nodes " + str(nbNodes))
    for i in range(nbNodes):
        print("v" + str(i), end=" ")
    print("")
    print("List of edges: ")
    for i in range(nbNodes):
        for j in range(nbNodes):
            if (mat[i][j] == 1):
                print("v" + str(i) + "-- v" + str(j) + " ")

showStruct(graph)



