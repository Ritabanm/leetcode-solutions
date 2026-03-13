class Solution:
    def maxPoints(self, technique1: List[int], technique2: List[int], k: int) -> int:
        n = len(technique1)
        res = [[technique1[i],technique2[i]] for i in range(n)]
        res.sort(key = lambda s:(s[0]-s[1]), reverse = True)
        tot = 0
        for i in range(k):
            tot+=res[i][0]
        for i in range(k,n):
            tot+=max(res[i][0], res[i][1])
        return tot