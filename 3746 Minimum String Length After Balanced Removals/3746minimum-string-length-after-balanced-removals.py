class Solution:
    def minLengthAfterRemovals(self, s: str) -> int:

        return abs(len(s) - 2 * s.count('a'))