'''
Write a function shortest_path that takes in an array of edges for an undirected graph and two npdes (nodeA, nodeB). The function should return the length of the shortest path between A and B. Consider the length as the number of edges in the path, not the number of nodes. If there is no path between A and B then return -1.
'''

def shortest_path(edges, nodeA, nodeB):
    graph = build_graph(edges)
    visited =  set( [ nodeA ] )
    queue = [ [nodeA, 0] ]
    while len(queue)  > 0:
        [current, distance] = queue.pop(0)
        if current == nodeB: return distance
        for neighbour in graph[current]:
            if neighbour not in visited:
                visited.add(neighbour)
                queue.append([neighbour, distance + 1])
    return -1


def build_graph(edges):
    graph = {}
    for edge in edges:
        [a, b] = edge
        if a not in graph: graph[a] = []
        if b not in graph: graph[b] = []
        graph[a].append(b)
        graph[b].append(a)
    return graph


edges = [
    ['i', 'j'],
    ['k', 'i'],
    ['m', 'k'],
    ['k', 'l'],
    ['o', 'n']
]

print(shortest_path(edges, 'i', 'm'))