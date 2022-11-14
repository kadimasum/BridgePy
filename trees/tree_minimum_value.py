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

def min_tree_value(root):
    if root ==  None: return float("inf")
    queue = [root]
    min_value = float("inf")
    while len(queue) > 0:
        current_node = queue.pop(0)
        min_value = min(min_value, current_node.data)

        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)

    return min_value

result = min_tree_value(five)
print(result)


