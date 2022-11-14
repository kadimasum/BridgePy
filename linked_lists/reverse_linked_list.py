'''
https://leetcode.com/problems/reverse-linked-list/

'''

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

def reverse_linked_list(head):
    prev = None
    current = head
    while current:
        temp =  current.next
        current.next = prev #Reverse
        prev = current #Iterate prev
        current = temp #Iterate current


    return prev

result = reverse_linked_list(a)

current = result
while current:
    print(current.data)
    current = current.next