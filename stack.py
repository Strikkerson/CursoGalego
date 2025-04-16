class ArrayStack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if len(self.items) == 0:
            raise IndexError("Can't pop from empty stack")
        
        return self.items.pop()

    def peek(self):
        if len(self.items) == 0:
            raise IndexError("Can't peek in empty stack")
        
        return self.items[-1]
    
    def size(self):
        return len(self.items)


class LimitedStack:
    def __init__(self, max_length=1000):
        self.items = [0] * max_length
        self.max_length = max_length
        self.pointer = 0   

    def push(self, item):
        if self.pointer == self.max_length:
            raise IndexError("Can't push in completely filled limited stack!")
        
        self.items[self.pointer] = item
        self.pointer += 1

    def pop(self):
        if self.pointer == 0:
            raise IndexError("Can't pop from empty stack!")

        popped_item, self.items[self.pointer-1] = self.items[self.pointer-1], 0
        self.pointer -= 1

        return popped_item
    
    def peek(self):
        if self.pointer == 0:
            raise IndexError("Can't peek in empty stack")
        
        return self.items[self.pointer-1]
    
    def size(self):
        return self.pointer


class Node:
    def __init__(self,val=0, next=None):
        self.val = val
        self.next = next

class LinkedStack:
    def __init__(self):
        self.top = None
        self._size = 0
    
    def push(self, val):
        node = Node(val)
        node.next = self.top
        self.top = node
        self._size += 1

    def pop(self):
        if not self.top:
            raise IndexError("Can't pop from empty stack!")
        
        popped_node = self.top
        self.top = self.top.next

        self._size -= 1

        return popped_node.val
    
    def peek(self):
        if not self.top:
            raise IndexError("Can't peek in empty stack")
        
        return self.top.val

    def size(self):
        return self._size

        


items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

stack = ArrayStack()
lim_stack = LimitedStack(10)
linked_stack = LinkedStack()

for item in items:
    stack.push(item)
    lim_stack.push(item)
    linked_stack.push(item)

for i in range(len(items)):
    print(f"Size: {stack.size()} | {lim_stack.size()} | {linked_stack.size()}")
    print(f"Popped Values: {stack.pop()} | {lim_stack.pop()} | {linked_stack.pop()}")



