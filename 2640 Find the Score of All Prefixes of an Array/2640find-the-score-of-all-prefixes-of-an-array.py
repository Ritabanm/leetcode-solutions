class Solution:
    def findPrefixScore(self, nums: List[int]) -> List[int]:
        res = []
        curr_max = 0
        sum = 0
        for num in nums:
            curr_max = max(curr_max, num)
            sum+=(num+curr_max)
            res.append(sum)
        return res