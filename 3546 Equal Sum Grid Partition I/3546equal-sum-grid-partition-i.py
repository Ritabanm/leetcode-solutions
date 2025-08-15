class Solution:
    def canPartitionGrid(self, grid: List[List[int]]) -> bool:
        def check(A):
            cur = 0
            for r in A:
                cur += sum(r)
                if cur + cur == total:
                    return True
            return False
        total = sum(sum(r) for r in grid)
        return check(grid) or check(zip(*grid))