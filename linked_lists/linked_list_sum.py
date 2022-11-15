class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

one = Node(1)
five = Node(5)
nine = Node(9)
three = Node(3)

one.next = five
five.next = nine
nine.next = three

def linked_list_sum(node):
    if node == None: return 0
    current = node
    sum = 0
    while current:
        sum += current.data
        current = current.next

    return sum

result = linked_list_sum(one)
print(result)
