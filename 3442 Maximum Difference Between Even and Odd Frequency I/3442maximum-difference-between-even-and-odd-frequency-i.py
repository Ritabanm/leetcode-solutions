class Solution:
    def maxDifference(self, s: str) -> int:
        maxOdd= 0
        minEve = float('inf')
        counts = Counter(s)
        for v in counts.values():
            if v%2==1:
                maxOdd = max(maxOdd, v)
            else:
                minEve= min(minEve, v)
        return maxOdd -minEve
        