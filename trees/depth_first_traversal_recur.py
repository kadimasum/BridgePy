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

def depthFirstTraversal(root):
    if root == None: return []
    left_values = depthFirstTraversal(root.left)
    right_values = depthFirstTraversal(root.right)
    return [root.value] + left_values + right_values

result = depthFirstTraversal(a)
print(result)