class Solution:
    def countSpecialSubsequences(self, nums):
        MOD = 10**9 + 7
        
        # Initialize counters for the counts of special subsequences ending with 0, 1, and 2
        count0, count1, count2 = 0, 0, 0
        
        # Number of 0s encountered so far
        zeros = 0
        
        for num in nums:
            if num == 0:
                # Each 0 can be part of all previous subsequences, plus itself
                zeros = (zeros * 2 + 1) % MOD
            elif num == 1:
                # Each 1 can be part of all subsequences formed by 0s
                count1 = (count1 * 2 + zeros) % MOD
            elif num == 2:
                # Each 2 can be part of all subsequences formed by 1s
                count2 = (count2 * 2 + count1) % MOD
        
        return count2
