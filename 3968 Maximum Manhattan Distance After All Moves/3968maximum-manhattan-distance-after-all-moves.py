class Solution:
    def maxDistance(self, moves: str) -> int:
        ct = Counter(moves)
        return abs(ct['U']-ct['D']) + abs(ct['L']-ct['R']) + ct['_']