class Solution:
    def isArraySpecial(self, nums:List[int])->bool:
        n = len(nums)
        pairs = []
        
        for i in range(1, n):
            if nums[i]&1==nums[i-1]&1:
                return False
        return True