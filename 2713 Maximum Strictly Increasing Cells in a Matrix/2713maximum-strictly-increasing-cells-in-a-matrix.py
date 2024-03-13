class Solution:
    def maxIncreasingCells(self, mat: List[List[int]]) -> int:
        m = len(mat)
        n = len(mat[0])
        
        # Positions of values
        pos = {}
        for r in range(m):
            for c in range(n):
                if mat[r][c] not in pos:
                    pos[mat[r][c]] = []
                pos[mat[r][c]].append((r, c))
        
        # the max_path starting from row or col with val-1
        prev_r = defaultdict(int)
        prev_c = defaultdict(int)
        
        for val in sorted(pos.keys(), reverse=True):
            
            # the max_path starting from row or col with val
            next_r = defaultdict(int)
            next_c = defaultdict(int)
            for r, c in pos[val]:
                next_r[r] = max(next_r[r], prev_r[r]+1, prev_c[c]+1)
                next_c[c] = max(next_c[c], prev_r[r]+1, prev_c[c]+1)

            # Update max paths
            prev_r.update(next_r)
            prev_c.update(next_c)

        # Answer is max_path from minimum value starting from any row or col
        return max(max(prev_r.values()), max(prev_c.values()))