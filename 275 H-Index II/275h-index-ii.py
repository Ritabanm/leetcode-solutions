class Solution:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        for idx, c in enumerate(citations):
            if c>=n-idx:
                return n-idx
        return 0
        