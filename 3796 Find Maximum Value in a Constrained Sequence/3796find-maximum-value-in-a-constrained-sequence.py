class Solution:
    def findMaxVal(self, n: int, restrictions: List[List[int]], diff: List[int]) -> int:
        upper_bound = [inf]*n
        upper_bound[0] = 0

        for idx, maxVal in restrictions:
            upper_bound[idx]=min(upper_bound[idx], maxVal)
        
        for i in range(1,n):
            upper_bound[i]=min(upper_bound[i], upper_bound[i-1]+diff[i-1])
        
        for i in range(n-2, -1, -1):
            upper_bound[i]=upper_bound[i]=min(upper_bound[i], upper_bound[i+1]
            +diff[i])
        return max(upper_bound)