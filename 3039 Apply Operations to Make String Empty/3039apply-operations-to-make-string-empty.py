class Solution:
    def lastNonEmptyString(self, s: str) -> str:
        freq = Counter(s)
        maxFreq = max(freq.values())
        res = ''
        for ch in reversed(s):
            if freq[ch] == maxFreq and ch not in res:
                res+=ch
        return res[::-1]