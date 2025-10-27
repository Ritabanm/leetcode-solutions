class Solution:
    def longestSubsequence(self, nums: List[int]) -> int:
        n = len(nums)
        dp ={}
        maxSoFar = 0
        for i in range(n):
            number = nums[i]
            maxSub = 1
            for diff in range(300,-1,-1):
                number1 = number-diff
                number2 = number+diff
                if(number1, diff) in dp:
                    maxSub = max(maxSub, dp[(number1, diff)]+1)
                if(number2, diff) in dp:
                    maxSub = max(maxSub, dp[(number2, diff)]+1)
                dp[(number, diff)] = maxSub
                maxSoFar = max(maxSoFar, maxSub)
        return maxSoFar
            
            
                

            
    