class Solution:
    def minimumSplits(self, nums: List[int]) -> int:

        gcd_ , ans = nums.pop(0), 1

        for num in nums:
            gcd_ = gcd(gcd_, num)
            
            if gcd_ == 1:
                ans += 1
                gcd_ = num

        return ans 