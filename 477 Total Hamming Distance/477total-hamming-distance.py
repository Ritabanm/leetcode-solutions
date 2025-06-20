class Solution:
    def totalHammingDistance(self, nums):
        total = 0
        n = len(nums)
        
        for bit in range(32):
            count_ones = sum((num >> bit) & 1 for num in nums)
            count_zeros = n - count_ones
            total += count_ones * count_zeros
        
        return total

                