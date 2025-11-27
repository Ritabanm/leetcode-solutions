class Solution:
    def matrixMedian(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])

        heap = [(row[0], r, 0) for r, row in enumerate(grid)]
        heapify(heap)
                
        for _ in range(m * n // 2):
            _, r, c = heapq.heappop(heap)
            if c < n - 1:
                heapq.heappush(heap, (grid[r][c+1], r, c+1))
            
        return heap[0][0]