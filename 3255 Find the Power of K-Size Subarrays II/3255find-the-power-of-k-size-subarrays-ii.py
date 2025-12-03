class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        cons =1
        res = []
        n = len(nums)
        for i in range(n):
            if i and nums[i]==1 + nums[i-1]:
                cons+=1
            else:
                cons =1
            if i+1>=k:
                if cons>=k:
                    res.append(nums[i])
                else:
                    res.append(-1)
        return res