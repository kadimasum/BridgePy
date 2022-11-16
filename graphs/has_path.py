graph = {
    'f':['g', 'i'],
    'g':['h'],
    'h':[],
    'i':['g', 'k'],
    'j':['i'],
    'k':[]
}

def has_path(graph, src, dst):
    queue = [ src ]
    while len(queue) > 0:
        current = queue.pop(0)
        if current == dst: return True
        for neighbour in graph[current]:
            queue.append(neighbour)

    return False

result = has_path(graph, 'f', 'j')
print(result)