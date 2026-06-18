class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        
        duplicates = []
        for i in range(len(nums)):
            num = abs(nums[i])-1
            if nums[num]>0:
                nums[num]*=-1
            else:
                duplicates.append(num+1)
        return duplicates
        