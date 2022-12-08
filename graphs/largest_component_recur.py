'''
Write a funcion largest component that takes in an adjacency list of an undirecteed graph. The function should return the size of the largest connected component in the graph
'''

def longest_component(graph):
    visited = set()
    longest = 0
    for node in graph:
        size = explore_size(graph, node, visited)
    return max(longest, size)


def explore_size(graph, node, visited):
    if node in visited: return 0
    size  = 1
    for neighbour in graph[node]:
        size = max(size, explore_size(graph, neighbour, visited))
    return size

graph = {
    'a':['b', 'c'],
    'b':['a','c'],
    'c':['a','b'],
    # 'd':[],
    # 'k':[]
}

print(longest_component(graph))