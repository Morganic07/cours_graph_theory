def add_edge(graph, u, v, w):
    graph.append([u, v, w])


def find_parent(parent, i):
    if parent[i] == i:
        return i
    return find_parent(parent, parent[i])


