
# Create a node 
class Node:
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

# Create the linked list class
class LinkedList:
    # Initialize the head to none
    def __init__(self) -> None:
        self.head = None

    # Insert at the begining of the linked list
    def insert_at_begining(self, data):
        node = Node(data, self.head)
        self.head = node

    # Print the linked list
    def print(self):
        if self.head is None:
            print("Linked list is empty.")
            return
        
        current = self.head

        while current :
            print(current.data)
            current = current.next

    # Insert at the end of the linked list
    def insert_at_end(self, data):
        if self.head == None:
            self.head= Node(data, None)
            return
        
        current = self.head

        while current.next:
            current = current.next

        current.next = Node(data, None)


    # Replace all values in the linked list with new values from the list
    def insert_values(self, data_list):
        self.head = None
        for data in data_list:
            self.insert_at_end(data)
        

    # Get the length of the linked list
    def get_length(self):

        count = 0

        current = self.head

        while current:
            count += 1
            current = current.next

        return count

    # Remove at index
    def remove_at(self, index):

        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index....")

        if index == 0: 
            self.head = self.head.next
            return

        count = 0
        current = self.head

        while current:

            if count == index - 1:
                current.next == current.next.next
                break
            
            current = current.next
            count += 1
    
    # Insert at index
    def insert_at(self, index, data):
        if index < 0 or index > self.get_length():
            raise Exception("Invalid index")

        if index == 0:
            self.insert_at_begining(data)
            return 

        count = 0
        current = self.head
        while current:
            if count == index - 1:
                node = Node(data, current.next)
                current.next = node
                break

            current = current.next
            count += 1





if __name__ == '__main__':
    li = LinkedList()
    li.insert_at_begining(5)
    li.insert_at_begining(3)
    li.insert_at_begining(8)
    li.insert_at_end(123)
    li.insert_at_begining(4)
    li.insert_at_end(7)
    li.insert_values(['mangoes', 'bananas', 'oranges'])
    print(li.get_length())
    li.insert_at(1,"Tomatto")
    li.remove_at(1)
    li.print()
