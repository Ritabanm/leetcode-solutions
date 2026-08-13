class Solution:
    def subsetsWithDup(self, nums):
        nums.sort()
        subsets = []
        currentSubset = []
        self.subsetsWithDupHelper(subsets, currentSubset, nums,0)
        return subsets
    
    def subsetsWithDupHelper(self, subsets, currentSubset, nums, index):
        subsets.append(list(currentSubset))
        for i in range(index, len(nums)):
            if i!=index and nums[i]==nums[i-1]:
                continue
            currentSubset.append(nums[i])
            self.subsetsWithDupHelper(subsets, currentSubset, nums, i+1)
            currentSubset.pop()     