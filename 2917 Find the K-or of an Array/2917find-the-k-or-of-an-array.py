class Solution:
    def findKOr(self, nums: List[int], k: int) -> int:
        # Handle the two edge cases 
        if k == 1: 
            return sum(nums) if len(nums) == 1 else nums[0] | self.findKOr(nums[1:], 1) 
        if k == len(nums): 
            return nums[0] & self.findKOr(nums[1:], len(nums) - 1) 

        result = 0 
        # since we know the maximum number is 2^31 - 1 
        for i in range(32):   
            count = sum((num >> i) & 1 for num in nums) 
            if count >= k: 
                result |= (1 << i) 

        return result 