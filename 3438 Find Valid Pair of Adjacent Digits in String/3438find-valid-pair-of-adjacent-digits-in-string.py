class Solution:
    def findValidPair(self, s: str) -> str:
        cnt = [0]*10
        zero = ord('0')
        for ch in s:
            cnt[ord(ch)-zero] += 1
        for i in range(len(s)-1):
            p1 = ord(s[i]) - zero
            p2 = ord(s[i+1]) - zero
            if p1 != p2 and cnt[p1] == p1 and cnt[p2] == p2:
                return s[i:i+2]
        return ""