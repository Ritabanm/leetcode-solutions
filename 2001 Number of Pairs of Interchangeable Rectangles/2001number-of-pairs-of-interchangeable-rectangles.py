from collections import Counter
from math import gcd

class Solution:
    def interchangeableRectangles(self, rectangles: list[list[int]]) -> int:
        freq = Counter()
        for w, h in rectangles:
            g = gcd(w, h)
            freq[(w // g, h // g)] += 1
        return sum(c * (c - 1) // 2 for c in freq.values())