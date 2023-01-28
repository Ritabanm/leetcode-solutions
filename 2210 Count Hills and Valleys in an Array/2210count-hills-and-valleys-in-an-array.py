class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        hill  = 0
        valley = 0

        filtered = [nums[0]]
        for i in range(1, len(nums)):
            if nums[i]!=nums[i-1]:
                filtered.append(nums[i])
            
        
        for i in range(1, len(filtered)-1):
            if filtered[i]>filtered[i-1] and filtered[i]> filtered[i+1]:
                hill+=1
            elif filtered[i]< filtered[i-1] and filtered[i]<filtered[i+1]:
                valley +=1
        
        return hill+valley