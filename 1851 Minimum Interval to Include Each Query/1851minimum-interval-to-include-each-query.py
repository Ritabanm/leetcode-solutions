class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort(reverse=True)
        heap = []
        ans = {}

        for q in sorted(queries):
            while intervals and intervals[-1][0] <= q:
                interval = intervals.pop()
                if interval[1] >= q:
                    heappush(heap, [interval[1] - interval[0] + 1, interval[1]])
            
            while heap and heap[0][1] < q:
                heappop(heap)
            
            ans[q] = heap[0][0] if heap else -1

        return [ans[q] for q in queries]
