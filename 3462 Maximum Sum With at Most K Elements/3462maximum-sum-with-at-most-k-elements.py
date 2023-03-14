class Solution:
    def maxSum(self, grid: List[List[int]], limits: List[int], k: int) -> int:
        res=0
        avilVal=[]
        for i in range(len(grid)):
            avilVal+=sorted(grid[i])[::-1][:limits[i]]
        res=sum(sorted(avilVal)[::-1][:k])
        return res