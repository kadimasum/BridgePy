class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.left = None
        self.right = None

a = Node("a")
b = Node("b")
c = Node("c")
d = Node("d")
e = Node("e")
f = Node("f")

a.left = b
a.right = c
b.left = d
b.right = e
c.right = f

def breath_first_traversal(root):
    if root == None: return []
    queue = [root]
    result = []
    while len(queue) > 0:
        cuerrent_node = queue.pop(0)
        result.append(cuerrent_node.value)
        if cuerrent_node.left: queue.append(cuerrent_node.left)
        if cuerrent_node.right: queue.append(cuerrent_node.right)

    return result

result = breath_first_traversal(a)
print(result)