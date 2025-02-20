from sortedcontainers import SortedList
from collections import deque

class MKAverage:
    def __init__(self, m: int, k: int):
        self.m = m
        self.k = k
        self.stream = deque()  # Stores the last m elements
        self.sorted_list = SortedList()  # Keeps elements sorted
        self.mid_sum = 0  # Sum of middle elements
    
    def addElement(self, num: int) -> None:
        self.stream.append(num)
        self.sorted_list.add(num)

        # If window exceeds m elements, remove the oldest element
        if len(self.stream) > self.m:
            oldest = self.stream.popleft()
            self.sorted_list.remove(oldest)

    def calculateMKAverage(self) -> int:
        if len(self.stream) < self.m:
            return -1  # Not enough elements
        
        # Get the middle elements by excluding k smallest and k largest
        mid_elements = self.sorted_list[self.k:self.m - self.k]
        return sum(mid_elements) // len(mid_elements)
