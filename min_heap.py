class MinHeap:
    def __init__(self):
        self.heap = []
        
    def _parent(self, index):
        return (index-1) // 2
        
    def _left_child(self, index):
        return index*2 + 1

    def _right_child(self, index):
        return index*2 + 2

    def _heapify_up(self, index):
        if index == 0:
            return
        
        parent_index = self._parent(index)

        if self.heap[parent_index] > self.heap[index]:
            self.heap[parent_index], self.heap[index] = self.heap[index], self.heap[parent_index]
            self._heapify_up(parent_index)
    
    def _heapify_down(self, parent_index):
        if parent_index == len(self.heap) - 1:
            return
        
        left = self._left_child(parent_index)
        right = self._right_child(parent_index)

        smallest = parent_index
        
        if left < len(self.heap) and  self.heap[left] < self.heap[smallest]:
            smallest = left

        if right < len(self.heap) and self.heap[right] < self.heap[smallest]:
            smallest = right

        if smallest != parent_index:
            self.heap[parent_index], self.heap[smallest] = self.heap[smallest], self.heap[parent_index]
            self._heapify_down(smallest)
    
    def insert(self, val):
        self.heap.append(val)
        self._heapify_up(len(self.heap) - 1)
    
    def pop_min(self):
        if len(self.heap) == 0:
            raise IndexError("Can't pop from empty heap!")
        
        if len(self.heap) == 1:
            return self.heap.pop()

        min_value = self.heap[0]

        self.heap[0] = self.heap.pop()
        self._heapify_down(0)

        return min_value

    def peek(self):
        if len(self.heap) == 0:
            raise IndexError("Can't peek in empty heap!")
        
        return self.heap[0]
    
    def size(self):
        return len(self.heap)
    
    def is_empty(self):
        return len(self.heap) == 0

    def display(self):
        print(self.heap)

min_heap = MinHeap()
min_heap.insert(0)
min_heap.insert(1)
min_heap.insert(2)
min_heap.insert(3)
min_heap.insert(4)
min_heap.insert(5)
min_heap.insert(0)

min_heap.display()
