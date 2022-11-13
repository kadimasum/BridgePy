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

def tree_includes(root, target):
    if root == None: return False
    if root.value == target: return True
    return tree_includes(root.left, target) or tree_includes(root.right, target)

result = tree_includes(a, 'k')
print(result)