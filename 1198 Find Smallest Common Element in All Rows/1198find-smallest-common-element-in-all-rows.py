class Solution:
    def smallestCommonElement(self, mat: List[List[int]]) -> int:
        M = iter(mat)
        S = set(next(M))
        for row in M:
            S &= set(row)
        return min(S, default=-1)