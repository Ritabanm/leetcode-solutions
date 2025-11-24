class Solution:
    def similarPairs(self, words: List[str]) -> int:

        words = [set   (w) for w in words]          # <–– 1)
        words = [sorted(w) for w in words]          # <–– 2)
        words = [tuple (w) for w in words]          # <–– 3)

        c = Counter(words)                          # <–– 4)
        
        return  sum(n*(n-1) for n in c.values())//2 # <–– 5)