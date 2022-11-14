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


'''
                    5
                    /\
                   2  6
                  / \    \
                1    4     7 
                 \
                  3
'''

def max_path_sum(root):
    if root == None: return float('-inf')
    if root.left == None and root.right == None: return root.data
    max_child_path_sum = max(max_path_sum(root.right), max_path_sum(root.left))
    return root.data + max_child_path_sum

result = max_path_sum(five)
print(result)