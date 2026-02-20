class Solution:
    def dominantIndices(self, nums: List[int]) -> int:

        cnt, sm, ans = len(nums), sum(nums), 0
 
        for num in nums:
            sm-= num
            cnt-= 1
            ans+= (num * cnt > sm)
            
        return ans