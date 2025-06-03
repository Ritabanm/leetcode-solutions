class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        idx = defaultdict(list)
        for i in range(len(nums)-1):
            for j in range(i+1, len(nums)):
                idx[nums[j]-nums[i]].append(i)
        
        count = 0 
        for i in range(len(nums)-3):
            for j in range(i+1, len(nums)-2):
                count += sum(k > j for k in idx[nums[i]+nums[j]])
                        
        return count