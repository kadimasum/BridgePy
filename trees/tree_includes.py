'''
write a function to find out if a tree includes a given value
'''
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
    stack = [root]
    while len(stack) > 0:
        current_node = stack.pop()
        if current_node.value == target: return True
        if current_node.right: stack.append(current_node.right)
        if current_node.left: stack.append(current_node.left)
    
    return False

result = tree_includes(a, "j")
print(result)