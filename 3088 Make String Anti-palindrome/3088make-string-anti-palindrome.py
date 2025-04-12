from collections import Counter
class Solution:
    def makeAntiPalindrome(self, s: str) -> str:
        counter = Counter(s) 
        n = len(s)
        if max(counter.values()) > n//2: return "-1"
        s = list(sorted(s))
        prefix = s[:n//2]
        suffix = s[n//2:]
        tailc = prefix[-1]
        resuffix = []
        j = 0
        while j < len(suffix) and suffix[j] == tailc:
            j += 1
        k = j
        i = 0
        while i < n//2 and prefix[-i-1] == tailc:
            resuffix.append(suffix[j])
            i += 1
            j += 1
        resuffix = resuffix + suffix[:k] + suffix[j:]
        return "".join(prefix + resuffix)