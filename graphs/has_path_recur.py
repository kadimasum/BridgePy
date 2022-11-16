'''
Write a function has_path that takes in an object representing the adjecency list of a directed acyclic graph and two nodes (src, dst). The function should return a boolean indicating whether or not there exists a directed path between the source and destination nodes.
'''

graph = {
    'f':['g', 'i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'j':['i'],
    'k':[]
}

def has_path(graph, src, dst):
    if src == dst: return True
    for neighbour in graph[src]:
        if has_path(graph, neighbour, dst):
            return True
    return False

result = has_path(graph, "f","j")
print(result)