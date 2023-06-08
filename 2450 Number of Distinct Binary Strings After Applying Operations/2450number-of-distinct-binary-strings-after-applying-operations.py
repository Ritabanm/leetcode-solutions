class Solution:
    def countDistinctStrings(self, s: str, k: int) -> int:
        mod = ((10 ** 9) + 7)
        #123456789
        #..
        # ..
        #  ..
        curlen = 0
        for i in range(len(s) - k + 1):
            curlen += 1
            #sub = s[i: i + k]
            #d["a"].append(sub)
        return (2 ** curlen) % mod
        