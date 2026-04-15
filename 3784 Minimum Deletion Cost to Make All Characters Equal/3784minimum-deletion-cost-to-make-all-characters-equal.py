class Solution:
    def minCost(self, s: str, cost: List[int]) -> int:
        scores = Counter()
        for char, cst in zip(s, cost):
            scores[char]+=cst
        total_cost = sum(cost)
        return min(total_cost-char_cost for char_cost in scores.values())