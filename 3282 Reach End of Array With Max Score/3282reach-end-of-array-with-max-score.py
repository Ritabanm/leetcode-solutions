class Solution:
    def findMaximumScore(self, nums: List[int], ans = 0) -> int:

        prev = nums.pop(0)
        
        for num in nums:
            ans+= prev 
            if num > prev: prev = num

        return ans