class Solution:
    def minimumGroups(self, words: List[str]) -> int:
        def get_min_cyclic_shift(s):
            n = len(s)
            if n <= 1: return s

            f = [-1] * (2 * n)
            k = 0
            for j in range(1, 2 * n):
                sj = s[j % n]
                i = f[j - k - 1]
                while i != -1 and sj != s[(k + i + 1) % n]:
                    if sj < s[(k + i + 1) % n]:
                        k = j - i - 1
                    i = f[i]

                if sj != s[(k + i + 1) % n]:
                    if sj < s[k]:
                        k = j
                    f[j - k] = -1
                else:
                    f[j - k] = i + 1

            return s[k:] + s[:k]

        unique_groups = set()
        for word in words:
            even_sub = word[0::2]
            odd_sub = word[1::2]

            _evens = get_min_cyclic_shift(even_sub)
            _odds = get_min_cyclic_shift(odd_sub)

            unique_groups.add((_evens, _odds))

        return len(unique_groups)