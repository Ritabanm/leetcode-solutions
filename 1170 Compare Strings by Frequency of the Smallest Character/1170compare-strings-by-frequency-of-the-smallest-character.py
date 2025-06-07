class Solution:
    def numSmallerByFrequency(
        self, queries: List[str], words: List[str]
    ) -> List[int]:
        f = lambda s: s.count(min(s))
        fW = sorted(map(f, words))
        return [len(words) - bisect_right(fW, f(q)) for q in queries]