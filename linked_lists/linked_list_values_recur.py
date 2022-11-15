class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d

def linked_list_values(node):
    values = []
    fill_values(node, values)
    return values

def fill_values(node, values):
    if node == None: return
    values.append(node.data)
    fill_values(node.next, values)