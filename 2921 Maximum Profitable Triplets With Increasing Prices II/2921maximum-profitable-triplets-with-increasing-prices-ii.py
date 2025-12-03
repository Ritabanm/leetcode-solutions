class FenwickTree:
    def __init__(self, n):
        self.size = n
        self.vals = [0] * (n + 1)
    
    def update(self, i, val):
        i += 1
        while i <= self.size:
            self.vals[i] = max(self.vals[i], val)
            i += i & -i

    def query(self, i):
        i += 1
        res = 0
        while i:
            res = max(res, self.vals[i])
            i -= i & -i
        return res

class Solution:
    def maxProfit(self, prices: List[int], profits: List[int]) -> int:
        n = len(prices)
        left = [0] * n
        right = [0] * n

        maxi = max(prices)
        tree1 = FenwickTree(maxi + 1)
        tree2 = FenwickTree(maxi + 1)

        for i, x in enumerate(prices):
            left[i] = tree1.query(x - 1)
            tree1.update(x, profits[i])

        for i in range(n-1, -1, -1):
            x = maxi + 1 - prices[i]
            right[i] = tree2.query(x - 1)
            tree2.update(x, profits[i])

        return max(
            (l + x + r for l, x, r in zip(left, profits, right) if l and r), default = -1
        )