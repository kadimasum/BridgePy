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

def print_linked_list(node):
    if node == None: return
    print(node.data)
    print_linked_list(node.next)

print_linked_list(a)