class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        N = len(pref)
        res = 0

        for w in words:
            if w[:N]==pref:
                res+=1
        return res
