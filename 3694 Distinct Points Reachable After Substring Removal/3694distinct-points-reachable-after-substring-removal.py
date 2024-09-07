class Solution:
    def distinctPoints(self, s: str, k: int) -> int:

        h = {'L': -1, 'R': 1, 'U': 0, 'D':  0}      # <-- 1)
        v = {'L':  0, 'R': 0, 'U': 1, 'D': -1}
        horz, vert, seen = 0, 0, {(0, 0)}

        for left, rght in zip(s, s[k:]):            # <-- 2)
            horz+= h[rght] - h[left]
            vert+= v[rght] - v[left]
    
            seen.add((horz, vert))

        return len(seen)                            # <-- 3)