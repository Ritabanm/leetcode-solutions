from heapq import heappush, heappop

class Solution:
    def getSkyline(self, buildings):
        events = []  # List of all critical points
        result = []  # Final skyline
        
        # Step 1: Convert buildings into events (left and right edges)
        for left, right, height in buildings:
            events.append((left, -height, right))  # Start of building
            events.append((right, height, None))   # End of building
        
        # Step 2: Sort events
        events.sort()  # Sorted by x-coord, then height

        # Step 3: Process events using a max heap
        max_heap = [(0, float('inf'))]  # Initial ground height (0)
        prev_max = 0  # Previous max height

        for x, h, r in events:
            if h < 0:  # Start of a building
                heappush(max_heap, (h, r))  # Push (-height, right)
            else:  # End of a building
                # Remove buildings that are beyond this x
                max_heap = [(h, r) for h, r in max_heap if r > x]
                heapq.heapify(max_heap)  # Rebuild heap

            # Get the current max height
            curr_max = -max_heap[0][0]

            # Step 4: Add to result if height changes
            if curr_max != prev_max:
                result.append([x, curr_max])
                prev_max = curr_max  # Update last recorded height

        return result
