class Solution:
    def minImpossibleOR(self, nums: List[int]) -> int:
        vals, ans = set(nums),0
        for i in range(31):
            val = 2**i
            if val in vals:
                ans+=val
                continue
            return ans+1

            