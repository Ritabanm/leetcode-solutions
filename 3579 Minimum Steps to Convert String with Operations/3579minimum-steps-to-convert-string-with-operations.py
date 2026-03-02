class Solution:
    def minOperations(self, word1: str, word2: str) -> int:
        n = len(word1)
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        def bestSwap(substr1, substr2):
            mismatches = [i for i in range(len(substr1)) if substr1[i] != substr2[i]]
            used = set()
            swaps = 0
            for i in mismatches:
                if i in used:
                    continue
                for j in mismatches:
                    if j <= i or j in used:
                        continue
                    if substr1[i] == substr2[j] and substr1[j] == substr2[i]:
                        swaps += 1
                        used.add(i)
                        used.add(j)
                        break
            total = len(mismatches)
            repls = total - 2 * swaps
            return swaps + repls

        def cost(substr1, substr2):
            if substr1 == substr2:
                return 0
            c1 = bestSwap(substr1, substr2)
            ar = substr1[::-1]
            c2 = 1 + bestSwap(ar, substr2)
            return min(c1, c2)

        for i in range(1, n + 1):
            for j in range(i):
                c = cost(word1[j:i], word2[j:i])
                dp[i] = min(dp[i], dp[j] + c)

        return dp[n]