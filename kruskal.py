def add_edge(graph, u, v, w):
    graph.append([u, v, w])


def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])


def union(parent, rank, x, y):
    xroot = find_parent(parent, x)
    yroot = find_parent(parent, y)

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1



def kruskal(graph, V):
    result = []
    i = 0
    e = 0
    graph = sorted(graph, key=lambda item: item[2])
    parent = [i for i in range(V)]
    rank = [0] * V

    while e < V - 1:
        u, v, w = graph[i]
        i = i + 1
        x = find_parent(parent, u)
        y = find_parent(parent, v)

        if x != y:
            e = e + 1
            result.append([u, v, w])
            union(parent, rank, x, y)
    
    return result 

