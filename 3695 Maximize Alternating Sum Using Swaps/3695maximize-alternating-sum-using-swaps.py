class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx != ry:
            if self.rank[rx] < self.rank[ry]:
                self.parent[rx] = ry
            elif self.rank[rx] > self.rank[ry]:
                self.parent[ry] = rx
            else:
                self.parent[ry] = rx
                self.rank[rx] += 1


class Solution:
    def maxAlternatingSum(self, nums, swaps):
        n = len(nums)
        dsu = DSU(n)

        for u, v in swaps:
            dsu.union(u, v)

        groups = {}
        for i in range(n):
            root = dsu.find(i)
            if root not in groups:
                groups[root] = []
            groups[root].append(i)

        new_nums = nums[:]
        for comp in groups.values():
            comp_vals = [nums[j] for j in comp]
            comp.sort()
            comp_vals.sort(reverse=True)
            even_idx = [idx for idx in comp if idx % 2 == 0]
            odd_idx = [idx for idx in comp if idx % 2 == 1]
            even_idx.sort()
            odd_idx.sort()
            assign = []
            for e in even_idx:
                assign.append((e, comp_vals.pop(0)))
            for o in odd_idx:
                if comp_vals:
                    assign.append((o, comp_vals.pop()))
            for pos, val in assign:
                new_nums[pos] = val

        max_sum = 0
        for i, val in enumerate(new_nums):
            if i % 2 == 0:
                max_sum += val
            else:
                max_sum -= val

        return max_sum