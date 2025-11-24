class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        prev , ans = 0, (0,0)
        for id,curr in logs:
            ans = min(ans, (prev-curr,id))
            prev =curr
        return ans[1]