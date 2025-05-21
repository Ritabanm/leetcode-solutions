class Solution:
    def minOperations(self, nums: List[int]) -> int:
        ans = toggle = 0
        for num in nums:
            if num == toggle:
                ans+=1
                toggle^=1
        return ans