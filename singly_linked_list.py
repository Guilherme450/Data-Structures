# Singly Linked List data structure.
# A linked list is a linear data structure.
# With it we can insert and remove data at run time O(1)

# Creating the class Node
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def remove(self, data):
        # Initializing the variables current and previous
        current = self.head
        previous = None

        while current is not None and current.data != data:
            previous = current
            current = current.next
        # if the data isn't found then the while loop will run until the Null. Therefore the current will be None because it's the tail.
        if current is None:
            # Tha data that was did request wasn't found, then return False!
            return False
        # Otherwise, it will verify if the pervious is None, if true we gonna go to the next node, else update the next node of previous node.
        if previous is None:
            self.head = current.next
        else:
            previous.next = current.next
        # If the required element was found then return True!
        return True

    def show(self):
        actual = self.head
        # while data exist it'll be true
        while actual:
            print(actual.data, end=' => ')
            actual = actual.next
        print('Null')

list = LinkedList()

list.add(2005)
list.add(1979)
list.add(1975)
list.add(2013)
list.add(2000)
list.remove(1975)

list.show()