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

def find(node, target):
    if node == None: return False
    current = node
    while current:
        if current.data == target: return True
        current = current.next

    return False

result = find(a, 'C')
print(result)