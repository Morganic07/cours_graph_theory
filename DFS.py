graph = {0:[2,5],
1:[0],
2:[1,5],
3:[1,6],
4:[0,5],
5:[None],
6:[3,5]}



def DFS(graph, node):
    visited = []

    if node not in visited:
        visited.append(node)
        print(node, end=" ")

        for neighbour in graph[node]:
            if neighbour is not None:
                DFS(graph, neighbour)
    
    


DFS(graph, 0)

