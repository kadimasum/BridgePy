'''
Write a function undirected_path that takes in an array of edges for an undirected graph and two nodes. (nodeA, nodeB). The function should return a boolean indicating whether or not there exists a path between nodeA and nodeB.


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

# Creating a graph from the edges
graph = {
    'i': ['j','k'],
    'j': ['i'],
    'k': ['i', 'm', 'l'],
    'm': ['k'],
    'l': ['k'],
    'o': ['n'],
    'n': ['o']
}

'''
edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

def undirected_path(edges, node_a, node_b):
    graph = build_graph(edges)
    return has_path(graph,node_a, node_b, set())


def build_graph(edges):
    graph  = {}
    for edge in edges:
        [a, b] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    
    return graph

def has_path(graph, src, dst, visited):
    if src == dst:
        return True
    if src in visited:
        return False
    visited.add(src)
    for neighbour in graph[src]:
        # if has_path(graph, neighbour, dst, visited) == True: return True
        if dst == neighbour: return True
    return False

print(undirected_path(edges, 'i', 'j'))