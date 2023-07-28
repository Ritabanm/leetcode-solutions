class Solution:
    def countPairs(self, words: List[str]) -> int:
        count = defaultdict(int)
        for w in words:
            base = ord(w[0])
            pat = []
            for ch in w:
                diff = (ord(ch)-base)%26
                pat.append(diff)
            count[tuple(pat)]+=1
        res = 0
        for i in count.values():
            res+=i*(i-1)//2
        return res