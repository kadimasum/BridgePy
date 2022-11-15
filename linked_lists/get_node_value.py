'''
Write a function that takes in the head of a linked list and an index. The function should return the value of the linked list at the specified index.
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

one = Node(1)
nine = Node(9)
seven = Node(7)
thirteen = Node(13)

one.next = nine
nine.next = seven
seven.next = thirteen

def get_node(head, index):
    if head == None: return float('inf')
    current = head
    count = 0
    while current:
        if count == index:
            return current.data
        current = current.next
        count += 1

    return float('inf')

result = get_node(one, 10)
print(result)
    