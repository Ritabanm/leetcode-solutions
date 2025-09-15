import bisect
class Solution:
    def shortestMatchingSubstring(self, s: str, p: str) -> int:
        first_star = p.find('*')
        second_star = p.find('*', first_star + 1)

        prefix = p[:first_star]
        middle = p[first_star + 1:second_star]
        suffix = p[second_star + 1:]

        if not prefix and not middle and not suffix:
            return 0

        len_pre, len_mid, len_suf = len(prefix), len(middle), len(suffix)
        mini = float('inf')

        # Rabin-Karp Rolling Hash for efficient substring search
        def rabin_karp(text, pattern):
            """Find all occurrences of pattern in text using Rabin-Karp."""
            if not pattern:
                return []
            base, mod = 256, 10**9 + 7  # Prime modulus
            pat_hash, text_hash, h = 0, 0, 1
            m, n = len(pattern), len(text)

            # Precompute hash multiplier (h = pow(base, m-1) % mod)
            for _ in range(m - 1):
                h = (h * base) % mod

            # Compute hash of pattern and first window
            for i in range(m):
                pat_hash = (base * pat_hash + ord(pattern[i])) % mod
                text_hash = (base * text_hash + ord(text[i])) % mod

            occurrences = []
            for i in range(n - m + 1):
                if pat_hash == text_hash and text[i:i + m] == pattern:
                    occurrences.append(i)
                if i < n - m:
                    # Rolling hash update
                    text_hash = (base * (text_hash - ord(text[i]) * h) + ord(text[i + m])) % mod
                    if text_hash < 0:
                        text_hash += mod

            return occurrences

        list_p, list_m, list_s = [], [], []
        
        if prefix:
            list_p = rabin_karp(s, prefix)
        if middle:
            list_m = rabin_karp(s, middle)
        if suffix:
            list_s = rabin_karp(s, suffix)

        # Binary search + two-pointer merge approach
        if prefix and middle and suffix:
            for i in list_p:
                idx_m = bisect.bisect_left(list_m, i + len_pre)
                if idx_m == len(list_m):
                    continue
                m_start = list_m[idx_m]
                idx_s = bisect.bisect_left(list_s, m_start + len_mid)
                if idx_s == len(list_s):
                    continue
                s_start = list_s[idx_s]
                mini = min(mini, s_start + len_suf - i)

        elif not prefix and middle and suffix:
            for m_start in list_m:
                idx_s = bisect.bisect_left(list_s, m_start + len_mid)
                if idx_s == len(list_s):
                    continue
                s_start = list_s[idx_s]
                mini = min(mini, s_start + len_suf - m_start)

        elif prefix and not middle and suffix:
            for i in list_p:
                idx_s = bisect.bisect_left(list_s, i + len_pre)
                if idx_s == len(list_s):
                    continue
                s_start = list_s[idx_s]
                mini = min(mini, s_start + len_suf - i)

        elif prefix and middle and not suffix:
            for i in list_p:
                idx_m = bisect.bisect_left(list_m, i + len_pre)
                if idx_m == len(list_m):
                    continue
                m_start = list_m[idx_m]
                mini = min(mini, (m_start + len_mid) - i)

        elif prefix and not middle and not suffix:
            if list_p:
                mini = len_pre

        elif not prefix and middle and not suffix:
            if list_m:
                mini = len_mid

        elif not prefix and not middle and suffix:
            if list_s:
                mini = len_suf

        return -1 if mini == float('inf') else mini