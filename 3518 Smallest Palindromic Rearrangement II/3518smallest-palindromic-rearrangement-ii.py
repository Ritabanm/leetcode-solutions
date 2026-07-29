from typing import List
class Solution:
    def smallestPalindrome(self, s: str, k: int) -> str:
        from math import comb
        n = len(s)
        freq = [0]*26
        for ch in s:
            freq[ord(ch)-97] += 1
        half_counts = [f//2 for f in freq]
        half_len = n//2
        def comb_with_cap(nm, r, cap):
            if r < 0 or r > nm:
                return 0
            r = r if r <= nm - r else nm - r
            res = 1
            for i in range(1, r+1):
                res = res * (nm - r + i) // i
                if res > cap:
                    return cap
            return res
        def count_multinomial(counts, cap):
            rem = sum(counts)
            res = 1
            for c in counts:
                if c == 0:
                    continue
                combv = comb_with_cap(rem, c, cap)
                res *= combv
                if res > cap:
                    return cap
                rem -= c
            return res
        total = count_multinomial(half_counts, k)
        if total < k:
            return ""
        half = []
        for pos in range(half_len):
            for ch in range(26):
                if half_counts[ch] == 0:
                    continue
                half_counts[ch] -= 1
                cnt = count_multinomial(half_counts, k)
                if cnt >= k:
                    half.append(chr(97+ch))
                    break
                else:
                    k -= cnt
                    half_counts[ch] += 1
            else:
                return ""
        mid = ""
        if n % 2 == 1:
            for i in range(26):
                if freq[i] % 2 == 1:
                    mid = chr(97+i)
                    break
        right = ''.join(reversed(half))
        return ''.join(half) + mid + right