class Solution:
    def minElement(self, nums: List[int]) -> int:
        ans = float('inf')
        for num in nums:
            k =num
            c = 0
            while k>0:
                c+=k%10
                k//=10
            ans = min(ans,c)
        return ans