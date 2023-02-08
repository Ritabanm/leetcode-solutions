class Solution:
    def minimumTimeToInitialState(self, word: str, k: int) -> int:
        n = len(word)
        z = [0] * n
        l, r = 0, 0

        for i in range(1, n):
            if i <= r:
                if z[i - l] + i <= r:
                    z[i] = z[i - l]
                else:
                    l = i
                    while r < n and word[r] == word[r - l]:
                        r += 1
                    z[i] = r - l
                    r -= 1
            else:
                l = r = i
                while r < n and word[r] == word[r - l]:
                    r += 1
                z[i] = r - l
                r -= 1

        result = 1
        i = k
        while i < n:
            if z[i] == n - i:
                return result
            i += k
            result += 1
        return result