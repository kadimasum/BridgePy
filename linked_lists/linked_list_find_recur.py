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
    if node.data == target: return True
    return find(node.next, target)

result = find(a, 'D')
print(result)