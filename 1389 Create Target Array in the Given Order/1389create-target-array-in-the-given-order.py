class Solution:    
    def createTargetArray(self, nums: List[int], ind: List[int]) -> List[int]:
        lst = []
        for i in range(len(nums)):
            lst.insert(ind[i], nums[i])
        return lst