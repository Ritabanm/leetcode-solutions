from collections import defaultdict
class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = defaultdict(list)
        for emp, mgr in enumerate(manager):
            if mgr != -1:
                adj[mgr].append(emp)
        def helper(mgr):
            if not adj[mgr]:
                return 0
            return informTime[mgr] + max(helper(ch) for ch in adj[mgr])
        return helper(headID)