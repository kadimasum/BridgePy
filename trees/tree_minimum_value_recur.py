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

five.left = two
five.right = six
two.left = one
two.right = four
six.right = seven
one.right = three

def min_value(root):
    if root == None: return float('inf')
    left_min = min_value(root.left)
    right_min = min_value(root.right)
    return min(root.data, left_min, right_min)

result = min_value(five)
print(result)