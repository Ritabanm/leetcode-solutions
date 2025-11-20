class Solution:
    def minSteps(self, s: str, t: str) -> int:
        counts = [0]*26
        a = ord('a')
        for ch in s:
            counts[ord(ch) - a] += 1
        for ch in t:
            counts[ord(ch) - a] -= 1
        return sum(abs(x) for x in counts)