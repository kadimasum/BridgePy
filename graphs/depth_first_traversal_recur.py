graph = {
    'a':['b','c'],
    'b':['d'],
    'c':['e'],
    'd':['f'],
    'e':[],
    'f':[]
}

def depth_first_print(graph, source):
    print(source)
    for neighbour in graph[source]:
        depth_first_print(graph, neighbour)

depth_first_print(graph, "a")