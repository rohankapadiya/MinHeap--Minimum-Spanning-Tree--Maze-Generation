# A class for a min heap
class MinHeap:
    
    def __init__(self, arr=[]):
        self.heap = []
        
        for i in arr:
            self.insert(i)

    def insert(self, element):
        self.heap.append(element)
        self.min_heap_up(len(self.heap)-1)
        

    def get_min(self):
        if len(self.heap) != 0:
            return self.heap[0]
        return None

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        
        minimum_value = self.heap[0]
        end_value = self.heap.pop()
        
        if len(self.heap) > 0:
            self.heap[0] = end_value
            self.min_heap_down(0)
            
        return minimum_value

    def is_empty(self):
        return len(self.heap) == 0

    def __len__(self):
        return len(self.heap)
    
    def min_heap_up(self, i):
        parent_value = (i-1)//2
        if parent_value >= 0:
            if self.heap[i] < self.heap[parent_value]:
                self.heap[i], self.heap[parent_value] = self.heap[parent_value], self.heap[i]
                self.min_heap_up(parent_value)
    
    def min_heap_down(self, i):
        left_side_value = 2*i+1
        right_side_value = 2*i+2
        small_value = i
        if left_side_value < len(self.heap):
            if self.heap[left_side_value] < self.heap[small_value]:
                small_value = left_side_value
        if right_side_value < len(self.heap):
            if self.heap[right_side_value] < self.heap[small_value]:
                small_value = right_side_value
        if small_value != i:
            self.heap[i], self.heap[small_value] = self.heap[small_value], self.heap[i]
            self.min_heap_down(small_value)
