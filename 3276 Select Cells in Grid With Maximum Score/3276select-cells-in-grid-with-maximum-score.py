class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:

        @lru_cache(None)
        def dp(i: int, mask: int)-> int:

            if i == len(values): return 0
            cur, value = mask, values[i]
            
            bits, j, res = d[value], 0, 0
            
            for _ in range(bits.bit_length()):

                if (bits%2,cur%2) == (1, 0):
                    res = max(res, value + dp(i + 1, mask | (1 << j)))
                j, bits, cur = j + 1, bits//2, cur//2
                
            if not res: res = dp(i + 1, mask)

            return res
        

        d = defaultdict(int)

        for idx, row in enumerate(grid):
            for num in row: d[num]|= (1<<idx)

        values = sorted(d, reverse = True)
        return dp(0, 0)