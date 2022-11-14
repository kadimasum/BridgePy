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
    if node == None: return []
    values = []
    current = node
    while current:
        values.append(current.data)
        current = current.next

    return values

result = linked_list_values(a)
print(result)