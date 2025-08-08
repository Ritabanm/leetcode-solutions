class Solution:
    def compute_lps_array(self, pattern):
        length = 0
        lps = [0] * len(pattern)
        i = 1

        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        return lps

    def KMP_search(self, text, pattern):
        m = len(pattern)
        n = len(text)
        lps = self.compute_lps_array(pattern)
        cnt = 0
        i = j = 0
        while i < n:
            if pattern[j] == text[i]:
                i += 1
                j += 1

            if j == m:
                cnt += 1
                j = lps[j - 1]
            elif i < n and pattern[j] != text[i]:
                if j != 0:
                    j = lps[j - 1]
                else:
                    i += 1
        return cnt

    def numberOfWays(self, A: str, B: str, k: int) -> int:
        MOD = 10**9 + 7
        ka, kb = A == B, self.KMP_search(A[1:] + A[:-1], B)
        n = len(A)
        f = (pow(n - 1, k, MOD) - pow(-1, k)) * pow(n, MOD - 2, MOD)
        return ((ka+kb)*f+ka*pow(-1,k))%MOD