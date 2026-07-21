class Solution:
    def minCost(self, source: str, target: str, rules: list[list[str]], costs: list[int]) -> int:
        n = len(source)

        dp = [math.inf] * (n + 1)
        dp[0] = 0
        wildcards = [p.count('*') for p, _ in rules]

        for i in range(1, n + 1):
            if (
                source[i - 1] == target[i - 1]
                and dp[i - 1] < dp[i]
            ): dp[i] = dp[i - 1]

            for idx, (pattern, replacement) in enumerate(rules):
                L = len(pattern)
                if i < L: continue
                l = i - L
                if dp[l] == math.inf: continue
                
                ok = True
                for j in range(L):
                    if pattern[j] != '*' and pattern[j] != source[l + j]:
                        ok = False
                        break
                    if replacement[j] != target[l + j]:
                        ok = False
                        break
                if ok:
                    cost = dp[l] + costs[idx] + wildcards[idx]
                    if cost < dp[i]: dp[i] = cost

        return dp[n] if dp[n] < math.inf else -1