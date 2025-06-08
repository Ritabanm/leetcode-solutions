class Solution:
    def countHighestScoreNodes(self, parents: List[int]) -> int:
        n = len(parents)
        scores = [1] * n
        graph = [[] for _ in range(n)]
        for e, i in enumerate(parents):
            if e: graph[i].append(e)
        def dfs(i):
            res = 1
            for j in graph[i]:
                val = dfs(j)
                res += val
                scores[i] *= val
            if i: scores[i] *= (n - res)
            return res
        dfs(0)
        return scores.count(max(scores))