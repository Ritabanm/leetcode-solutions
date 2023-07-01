class Solution:
    def longestCycle(self, edges: List[int]) -> int:
        start = -2
        ans = -1

        for i in range(len(edges)):
            if edges[i] >= 0:
                offset = start
                cur = i
                while 1:
                    if edges[cur] < 0:
                        if edges[cur] <= offset:
                            ans = max(ans, edges[cur] - start)
                        break
                    nxt = edges[cur]
                    edges[cur] = start
                    start -= 1
                    cur = nxt
        
        return ans