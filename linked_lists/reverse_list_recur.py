class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None


a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')

a.next = b
b.next = c
c.next = d


def reverse_linked_list(head, prev=None):
    if head == None: return prev
    next = head.next
    head.next = prev
    return reverse_linked_list(next, head)



result = reverse_linked_list(a)

current = result
while current:
    print(current.data)
    current = current.next