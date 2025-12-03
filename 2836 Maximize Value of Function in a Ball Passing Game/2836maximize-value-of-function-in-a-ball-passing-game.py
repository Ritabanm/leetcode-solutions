class Solution:
    def getMaxFunctionValue(self, receiver: List[int], k: int) -> int:
        child, cost = defaultdict(list), defaultdict(list)
        n = len(receiver)
        t = len(bin(k)) - 2
        for i in range(t):
            for v in range(n):
                ch = child[child[v][i-1]][i-1] if i > 0 else receiver[v]
                child[v].append(ch)
                co = cost[v][i-1] + cost[child[v][i-1]][i-1] if i > 0 else receiver[v]
                cost[v].append(co)
        
        ans = 0
        for v in range(n):
            _sum, node = v, v
            need = bin(k)[2:][::-1]
            for i in range(t):
                if need[i] == '1':
                    _sum += cost[node][i]
                    node = child[node][i]
            ans = max(ans, _sum)
        return ans