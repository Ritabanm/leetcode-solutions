"""class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        if max(nums)==0:
            return 0
        if reduce(xor, nums)==0:
            return n-1
        return n"""

class Solution:
    def longestSubsequence(self, nums):
        n = len(nums)
        if max(nums)==0:
            return 0
        if reduce(xor, nums)==0:
            return n-1
        return n