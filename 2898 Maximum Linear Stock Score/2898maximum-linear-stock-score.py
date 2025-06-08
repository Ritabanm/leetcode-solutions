class Solution:
    def maxScore(self, prices: List[int]) -> int:
        same_origin = defaultdict(int)
        for i, p in enumerate(prices):
            same_origin[p-i]+= p
        return max(same_origin.values())