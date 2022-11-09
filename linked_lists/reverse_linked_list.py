'''
https://leetcode.com/problems/reverse-linked-list/

'''

def reverse_linked_list(head):
    prev = None
    current = head
    while head:
        temp =  current.next
        current.next = prev #Reverse
        prev = current #Iterate prev
        current = temp #Iterate current

    return prev

