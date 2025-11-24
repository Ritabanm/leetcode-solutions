class Solution:
    def seePeople(self, h: List[List[int]]) -> List[List[int]]:
        m, n = len(h), len(h[0])
        res = [[0]*n for _ in range(m)]
        for i in range(m):
            stack = []
            for j in range(n-1,-1,-1):
                e = h[i][j]
                while stack and h[i][stack[-1]] < e:
                    stack.pop()
                    res[i][j] += 1
                if stack:
                    if h[i][stack[-1]] == e:
                        stack.pop()
                    res[i][j] += 1
                stack.append(j)
        for j in range(n):
            stack = []
            for i in range(m-1,-1,-1):
                e = h[i][j]
                while stack and h[stack[-1]][j] < e:
                    stack.pop()
                    res[i][j] += 1
                if stack:
                    if h[stack[-1]][j] == e:
                        stack.pop()
                    res[i][j] += 1
                stack.append(i)
        return res
                