class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        ans = float('inf')
        for i in nums:
            if abs(i)<abs(ans) or (abs(i)==abs(ans) and i>ans):
                ans = i
        return ans 