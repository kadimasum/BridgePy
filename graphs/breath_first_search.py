
graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

def breath_first_print(graph, source):
    queue = [ source ]
    while len(queue) > 0:
        current = queue.pop(0)
        print(current)
        for neighbour in graph[current]:
            queue.append(neighbour)

breath_first_print(graph, 'a')