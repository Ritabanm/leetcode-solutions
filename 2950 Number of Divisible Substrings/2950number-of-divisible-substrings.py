class Solution:
    def countDivisibleSubstrings(self, word: str) -> int:
        chr_digit_map = {}
        for i in range(26):
            chr_digit_map[chr(97 + i)] = (i + 4) // 3
        
        n = len(word)
        ans = 0
        for st_idx in range(n):
            idx = st_idx
            thissum = 0
            thislen = 0
            while idx < n:
                thislen += 1
                thissum += chr_digit_map[word[idx]]
                if thissum % thislen == 0:
                    ans += 1
                idx += 1
        
        return ans