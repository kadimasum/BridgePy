'''
Write a funtion connected_components_count, that takes in an adjacency list of an undirected graph. The function should return the number of connected components within the graph.
'''
def connected_components_count(graph):
    visited = set()
    count = 0
    def dfs(node):
        for neighbour in graph[node]:
            if neighbour not in visited:
                visited.add(neighbour)
                dfs(neighbour)
    for node in graph:
        if node in visited:
            continue
        else:
            visited.add(node)
            count += 1
            dfs(node)
    return count

graph = {
    'a':['b', 'c'],
    'b':['a','c'],
    'c':['a','b'],
    'd':[],
    'k':[]
}

print(connected_components_count(graph))