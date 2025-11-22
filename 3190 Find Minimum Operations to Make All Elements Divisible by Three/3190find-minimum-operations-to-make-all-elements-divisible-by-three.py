class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        x = 0
        for i in nums:
            if i%3!=0:
                x+=1
        return x