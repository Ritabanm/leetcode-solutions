import heapq
import math

class Solution:
    def pickGifts(self, gifts: list[int], k: int) -> int:
        # Convert gifts array to a max-heap by pushing negative values
        max_heap = [-gift for gift in gifts]
        heapq.heapify(max_heap)
        
        # Perform the operations for k seconds
        for _ in range(k):
            # Pop the largest pile (negative value for max-heap simulation)
            max_gifts = -heapq.heappop(max_heap)
            
            # Reduce the pile to the floor of its square root
            reduced_gifts = math.floor(math.sqrt(max_gifts))
            
            # Push the reduced value back into the heap (as negative for max-heap)
            heapq.heappush(max_heap, -reduced_gifts)
        
        # Sum up the remaining values in the heap (convert back to positive)
        return -sum(max_heap)
