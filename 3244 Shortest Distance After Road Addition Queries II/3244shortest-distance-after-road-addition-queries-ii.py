from sortedcontainers import SortedList
class Solution:
    def eraseMiddleNodes(self, s, l, r):
        start = s.bisect_left(l)
        end = s.bisect_right(r)
        del s[start:end]

    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        s = SortedList(range(n))
        ans = []        
        for x, y in queries:
            self.eraseMiddleNodes(s, x + 1, y - 1)
            ans.append(len(s) - 1)        
        return ans