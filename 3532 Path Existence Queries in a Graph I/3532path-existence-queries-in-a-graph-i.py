class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:

        c, id = [0]*n, 0
        for i in range(1, n):
            if nums[i]-nums[i-1]<=maxDiff:
                c[i]=id
            else:
                id+=1
                c[i]=id
        return [c[u]==c[v] for u,v in queries]
        