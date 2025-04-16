class Node:
    def __init__(self, val, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_to_end(self, val):
        node = Node(val)

        if not self.tail:
            self.head = self.tail = node
        else:
            node.prev = self.tail
            self.tail.next = Node(val)
            self.tail = self.tail.next

    def add_to_front(self, val):
        node = Node(val)

        if not self.head:
            self.head = self.tail = node
        else:
            self.head.prev = node
            node.next = self.head
            self.head = node
    
    