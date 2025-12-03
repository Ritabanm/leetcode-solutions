class Solution:
    def maxScore(self, n: int, edges: List[List[int]]) -> int:
        return n*(n+1)*(2*n+1)//6 - 2*n + 1 + 2*(len(edges) == n)