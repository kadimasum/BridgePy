class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def traversal(self):
        first = self.head
        while first:
            print(first.data)
            first = first.next

    def insert_new_header(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node

    def search(self, x):
        temp = self.head
        while temp is not None:
            if temp.data == x:
                return True
            temp = temp.next
        else:
            return False

    def delete_node(self, data):
        temp = self.head
        while temp is not None:
            if temp.data == data:
                break
            prev = temp
            temp = temp.next
            prev.next = temp.next

    def delete_tail(self):
        temp = self.head
        while temp.next.next is not None:
            temp = temp.next
        temp.next = None



family = LinkedList()
family.head = Node("Bob")
wife = Node("Amy")
first_kid = Node("John")
second_kid = Node("Jane")

family.head.next = wife
wife.next = first_kid
first_kid.next = second_kid


family.insert_new_header("Sam")
# print(family.search("Johtn"))
family.delete_node("Amy")
family.delete_tail()
family.traversal()