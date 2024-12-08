class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        ans =-1
        for i in nums:
            for j in nums:
                # if exists number j such that i. is negative of j. 
                if i==-j:
                    ans = max(ans, abs(i))
        return ans