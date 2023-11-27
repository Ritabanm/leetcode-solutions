class Solution:
    def maxSumDistinctTriplet(self, x: List[int], y: List[int]) -> int:

        d = defaultdict(int)

        for numX, numY in zip(x, y):
            d[numX] = max(d[numX], numY)

        if len(d.values()) < 3: return -1
    
        return sum(nlargest(3, d.values()))    

        