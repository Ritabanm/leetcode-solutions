class Solution:
    def numSplits(self, s: str) -> int:
        d1 = Counter(s)
        d2 = defaultdict(int)

        count = 0
        for i in s:
            d2[i]+=1
            d1[i]-=1
            if d1[i]==0:
                del d1[i]
            if len(d2)==len(d1):
                count+=1
        return count