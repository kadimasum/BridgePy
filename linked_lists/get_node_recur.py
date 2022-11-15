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
    if head == None: return None
    if index == 0: return head.data
    return get_node(head.next, index - 1)



result = get_node(one, 1)
print(result)