class Solution:
    def numberOfPaths(self, n: int, corridors: List[List[int]]) -> int:
        d = defaultdict(set)
        for u, v in corridors:
            d[v-1].add(u-1)
            d[u-1].add(v-1)
        def triangle(node):
            cnt = 0
            for n1, n2 in itertools.combinations(d[node], 2):
                if n2 in d[n1]:
                    cnt += 1
            return cnt
        res = 0
        for i in range(n):
            res += triangle(i)
        return res//3