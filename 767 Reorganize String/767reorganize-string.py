from collections import Counter
import heapq

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Step 1: Count frequency of each character
        count = Counter(s)
        
        # Step 2: Create a max heap (invert the count for max heap using negative values)
        maxHeap = [[-cnt, char] for char, cnt in count.items()]
        heapq.heapify(maxHeap)  # Transform the list into a heap
        
        # prev keeps track of the last character used
        prev = None
        res = ""  # This will hold our result string

        # Step 3: Start processing the heap
        while maxHeap or prev:
            if prev and not maxHeap:
                # If we have a previous character but no characters left in the heap,
                # it means we can't place the previous character without causing an adjacent duplicate.
                return ""

            # Step 4: Get the most frequent character
            cnt, char = heapq.heappop(maxHeap)
            res += char  # Append the character to the result
            cnt += 1     # Decrement its count (remember cnt is negative)

            # Step 5: Push the previous character back to the heap if it still has occurrences left
            if prev:
                heapq.heappush(maxHeap, prev)
                prev = None  # Reset prev

            # Step 6: If the current character still has occurrences left, store it as prev
            if cnt != 0:  # cnt is negative, so non-zero means there are still occurrences left
                prev = [cnt, char]

        return res  # Return the reorganized string
