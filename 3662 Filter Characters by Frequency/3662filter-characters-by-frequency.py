class Solution:
    def filterCharacters(self, s: str, k: int) -> str:
        ctr = defaultdict(int)
        for ch in s:
            ctr[ch]+=1
        for c, cnt in ctr.items():
            if cnt>=k:
                s = s.replace(c, '')
        return s