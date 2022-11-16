'''
Write a function zipperlists that takes in the head of two linked lists as arguments, The function should zipper the two lists together into single linked lists by alternating nodes. If one of the two linked lists is longer than the other the resulting list should terminate with the remaining nodes. The function should return the head of the zipped linked list.

Do this in place, by mutating thee origiinal nodes
You may assume that both input lists are non-empty

list_1 = a->b->c
list_2 = v->w->x->y->z
output= a->v->b->w->c->x->y->z
'''
class Node:
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

a = Node('A')
b = Node('B')
c = Node('C')
d = Node('D')
e = Node('E')
f = Node('F')
g = Node('G')

x = Node('X')
y = Node('Y')
z = Node('Z')


a.next = b
b.next = c
c.next = d
d.next = e
e.next = f
f.next = g

x.next = y
y.next = z


def zipper_lists(head1, head2):
    tail = head1
    current1 = head1.next
    current2 = head2
    count = 0
    while current1 and current2:
        if count % 2 == 0:
            tail.next = current2
            current2 = current2.next
        else:
            tail.next = current1
            current1 = current1.next
        
        tail = tail.next
        count += 1

    if current1: tail.next = current1
    if current2: tail.next = current2
    
    
    return head1


result = zipper_lists(a, x)

current =  result
while current:
    print(current.data)
    current = current.next