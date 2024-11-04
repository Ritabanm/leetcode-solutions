class Solution:
    def countAnagrams(self, s: str) -> int:
        from math import factorial
        words = s.split()
        n_anagrams = 1
        mod = 10 ** 9 + 7
        for word in words:
            n_perms = math.factorial(len(word))
            letters = {}
            for letter in word:
                if (letter in letters):
                    letters[letter] += 1
                else:
                    letters[letter] = 0
            for letter in letters:
                if letters[letter]:
                    n_perms //= math.factorial(letters[letter] + 1)
            n_anagrams = (n_anagrams % mod) * (n_perms % mod)
        return int(n_anagrams) % mod