class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
    # Initialize variables
        sum_indices = {}  # To store the earliest index of each cumulative sum
        current_sum = 0  # Running cumulative sum
        max_length = 0  # Maximum length of subarray

        for i, num in enumerate(nums):
            current_sum += num

            # Case 1: Subarray from the start has sum k
            if current_sum == k:
                max_length = i + 1

            # Case 2: Subarray sum equals k using prefix sum
            if current_sum - k in sum_indices:
                max_length = max(max_length, i - sum_indices[current_sum - k])

            # Store the earliest index of current_sum
            if current_sum not in sum_indices:
                sum_indices[current_sum] = i

        return max_length