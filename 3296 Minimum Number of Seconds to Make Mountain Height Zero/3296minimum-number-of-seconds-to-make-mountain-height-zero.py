class Solution:
    def minNumberOfSeconds(self, mountainHeight: int, workerTimes: List[int]) -> int:
        min_heap = [(t, 1, t) for t in workerTimes]
        heapq.heapify(min_heap)
        for _ in range(mountainHeight):
            t, idx, base = heapq.heappop(min_heap)
            heapq.heappush(min_heap, (t + base * (idx + 1), idx + 1, base))
        return t