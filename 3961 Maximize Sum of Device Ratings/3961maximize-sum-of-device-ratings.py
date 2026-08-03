class Solution:
    def maxRatings(self, mat: List[List[int]]) -> int:
        n = len(mat)
        m = len(mat[0])
        mini = 0
        minVal = math.inf

        if m == 1:
            ans = 0
            for i in range(n):
                ans += mat[i][0]
            return ans

        for i in range(n):
            mat[i].sort()
            if mat[i][1] < mat[mini][1]:
                mini = i
            minVal = min(minVal, mat[i][0])
    
        ans = minVal

        for i in range(n):
            if i == mini:
                continue
            else:
                ans += mat[i][1]
        
        return ans