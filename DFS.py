graph = {0:[2,5],
1:[0],
2:[1,5],
3:[1,6],
4:[0,5],
5:[None],
6:[3,5]}



def DFS(graph, node):
    if visited== FALSE:
        for i in graph.keys():
            print("noeud", i, "visité\n")
            visited = TRUE

    elif visited==TRUE:
        DFS(graph, node)
    
    


DFS(graph, 0)
