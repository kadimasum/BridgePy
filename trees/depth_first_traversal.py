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

def depth_first_traversal(root):
    stack = [root]
    while len(stack) > 0:
        current_node = stack.pop()
        print(current_node.value)
        if current_node.right: stack.append(current_node.right)
        if current_node.left: stack.append(current_node.left)

depth_first_traversal(a)