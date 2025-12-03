class Solution:
    def baseUnitConversions(self, conversions: List[List[int]]) -> List[int]:
        vs = defaultdict(dict)
        for u, v, w in conversions:
            vs[u][v] = w
            vs[v][u] = w

        result = [-1] * (len(conversions) + 1)
        result[0] = 1

        modulo = 10 ** 9 + 7
        stack = [0]
        while stack:
            u = stack.pop()
            for v, w in vs[u].items():
                if result[v] == -1:
                    result[v] = (result[u] * w) % modulo
                    stack.append(v)
        
        return result