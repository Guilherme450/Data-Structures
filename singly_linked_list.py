# Singly Linked List data structure.
# A linked list is a linear data structure.
# With it we can insert and remove data at run time O(1)

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Sll:
    def __init__(self):
        self.head = None

    def add(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def remove(self, index):
        current_index = 0
        current_node = self.head
        previous = None

        while current_node is not None and current_index != index:
            current_index += 1
            previous = current_node
            current_node = current_node.next

        if current_node is None:
            print(f'Element at index {index} not found!')
            return False

        if previous is None:
            self.head = current_node.next
        else:
            previous.next = current_node.next

        print(f'Element at index: {index} removed!')
        return True

    def search(self, index):
        current_index = 0
        current_node = self.head

        while current_node is not None and current_index != index:
            current_index += 1
            current_node = current_node.next

        if current_node is None:
            print(f'Element at index {index} not found!')
            return False
        else:
            print(f'element: {current_node.data} at index: {index}')

    def show(self):
        current_node = self.head
        current_index = 0

        while current_node:
            print(f'index: {current_index} value: ({current_node.data})')
            current_index += 1
            current_node = current_node.next
        print('Null')
        print('-------------------')

list = Sll()

list.add(18)
list.add(20)
list.add(45)
list.add(10)
list.add(56)
list.add(12)
list.search(0)

list.show()

list.remove(2)

list.show()
list.search(2)