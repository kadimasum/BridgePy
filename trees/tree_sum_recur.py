class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.left = None
        self.right = None

one = Node(1)
two = Node(2)
three = Node(3)
four = Node(4)
five = Node(5)
six = Node(6)
seven = Node(7)

one.left =  two
one.right = three
two.left = four
two.right = five
three.left = six
three.right = seven

def tree_sum(root):
    if root == None: return 0
    return root.data + tree_sum(root.left) + tree_sum(root.right)

result = tree_sum(one)
print(result)