class Solution:
    def minBishopMoves(self, source: list[int], target: list[int]) -> int:
        if (source[0] + source[1])%2!= (target[0] + target[1])%2:
            return -1
        if (source[1]-target[1])!=0:
            slope = (source[0]-target[0])/(source[1]-target[1])
            if abs(slope)==1:
                return 1
        return 2