class Solution:
    def minDifference(self, nums: List[int], 
                         queries: List[List[int]]) -> List[int]:

        ans, dp = [], [[0]*(max(nums)+1)]

        for num in nums:
            newRow = dp[-1].copy()
            newRow[num]+= 1
            dp.append(newRow)

        for left, right in queries:
            idx = [i for i,(r,l) in enumerate(zip(dp[right+1],
                                          dp[left])) if r > l]

            ans.append(min((i-j for i,j in zip(idx[1:],idx))
                                               ,default = -1))
        
        return  ans