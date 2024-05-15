class Solution:
    def maximumSumScore(self, nums: List[int]) -> int:
        prefix = [0]
        for num in nums: 
            prefix.append(prefix[-1]+num)
        
        result = -math.inf
        for i, num in enumerate(nums):
            result = max(result, max(prefix[i+1], 
            prefix[len(prefix)-1]-prefix[i]))
        return result