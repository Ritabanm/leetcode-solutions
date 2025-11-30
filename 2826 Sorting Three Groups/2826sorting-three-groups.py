class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        
        nIsNot = lambda x: int(x != n)
        
        n = nums.pop(0)
        dp1, dp2, dp3 = nIsNot(1), nIsNot(2), nIsNot(3)

        for n in nums:
            dp1, dp2, dp3 = ( dp1                + nIsNot(1),
                              min(dp1, dp2)      + nIsNot(2),
                              min(dp1, dp2, dp3) + nIsNot(3) )

        return min(dp1, dp2, dp3)