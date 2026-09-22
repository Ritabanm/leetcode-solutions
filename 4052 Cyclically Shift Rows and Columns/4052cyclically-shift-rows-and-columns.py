class Solution:
    def cyclicShift(self, n, g, rowShift, colShift):
        R, C = len(g), len(g[0])
        for r, mov in enumerate(rowShift): 
            mov %= C; g[r] = g[r][mov:] + g[r][:mov]            
        for c, mov in enumerate(colShift):
            vals = [g[(r + mov) % R][c] for r in range(R)]
            for r in range(R): g[r][c] = vals[r]
        return g       