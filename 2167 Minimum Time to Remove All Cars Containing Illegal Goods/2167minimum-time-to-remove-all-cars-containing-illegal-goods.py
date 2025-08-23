class Solution:
    def minimumTime(self, s: str) -> int:
        # Step 1: Initialize variables
        length = len(s)  # Total length of the string
        start = 0         # Time spent on removing cars up to the current position
        res = length      # Initialize the result with the maximum possible value (all cars removed via middle operation)

        # Step 2: Iterate through the string to find the optimal time
        for i, c in enumerate(s):
            # Case 1: If the current car contains illegal goods ('1'),
            # we can remove it from the middle, which takes 2 units of time.
            # Case 2: If we encounter a '0', we don't need to remove it.
            start = min(start + (c == "1") * 2, i + 1)
            
            # Case 3: We compute the total time if we were to remove all cars
            # from the start to the current position and then from the current
            # position to the end of the string.
            res = min(res, start + length - 1 - i)
        
        # Step 3: Return the minimal time
        return res