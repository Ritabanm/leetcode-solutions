class Solution:
    def findScore(self, nums: List[int]) -> int:
        
        n = len(nums)
        marked = [False] * n  # Array to track marked elements
        score = 0

        # Pair each number with its index, and sort by value, then by index
        sorted_nums = sorted((num, i) for i, num in enumerate(nums))

        for num, index in sorted_nums:
            # If the current element is not already marked
            if not marked[index]:
                # Add the value of the current element to the score
                score += num

                # Mark the current element
                marked[index] = True
                # Mark its left adjacent element if it exists
                if index > 0:
                    marked[index - 1] = True
                # Mark its right adjacent element if it exists
                if index < n - 1:
                    marked[index + 1] = True

        return score