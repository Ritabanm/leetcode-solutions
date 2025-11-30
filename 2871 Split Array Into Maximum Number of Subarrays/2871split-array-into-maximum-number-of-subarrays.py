mx = 1048575  #  <-- which is 11111111111111111111 base 2

class Solution:
    def maxSubarrays(self, nums: List[int]) -> int:

        ans, acc = 0, mx

        for num in nums:
            acc&= num
    
            if acc == 0 :
                ans+= 1 
                acc = mx

        return 1 if ans == 0 else ans 