class Solution:
    def minCost(self, startPos: List[int], homePos: List[int], rowC: List[int], colC: List[int]) -> int:
        m, n = len(rowC), len(colC)
        i1, j1 = startPos
        i2, j2 = homePos
        ans = 0
        if(i1 <= i2):
            for i in range(i1+1, i2+1):
                ans += rowC[i]
        else:
            for i in range(i1-1, i2-1, -1):
                ans += rowC[i]
        if(j1 <= j2):
            for j in range(j1+1, j2+1):
                ans += colC[j]
        else:
            for j in range(j1-1, j2-1, -1):
                ans += colC[j]
        return ans