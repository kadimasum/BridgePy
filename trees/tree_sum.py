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
    sum = 0
    queue = [root]
    while len(queue) > 0:
        current_node = queue.pop(0)
        sum += current_node.data
        if current_node.left: queue.append(current_node.left)
        if current_node.right: queue.append(current_node.right)
    
    return sum

result = tree_sum(one)
print(result)

