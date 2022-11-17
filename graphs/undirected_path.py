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