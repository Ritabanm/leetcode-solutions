class Solution:
    def fairCandySwap(self, aliceSizes: List[int], bobSizes: List[int]) -> List[int]:
        delta = (sum(bobSizes)-sum(aliceSizes))//2
        for a in aliceSizes:
            if a+delta in bobSizes:
                return [a, a+delta]