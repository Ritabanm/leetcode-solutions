class Solution:
    def kthSmallest(self, mat: List[List[int]], k: int) -> int:
        m, n = len(mat), len(mat[0])

        # Process one pair of rows (results) at a time.    
        def one_pair(curr, prev):
            heap = []
            heappush(heap, (curr[0] + prev[0], 0, 0))
            count = 0
            res = []
            while heap and count < k:
                val, i, j = heappop(heap)
                res.append(val)
                if j == 0 and i+1 < len(curr):
                    heappush(heap, (curr[i+1] + prev[0], i+1, 0))
                if j+1 < len(prev):
                    heappush(heap, (curr[i] + prev[j+1], i, j+1))
                count += 1
            return res

        
        # Start from the bottom and working its way up.
        prev = mat[m-1][:k]
        for i in range(m-2, -1, -1):
            prev = one_pair(mat[i], prev)
        return prev[-1]

            