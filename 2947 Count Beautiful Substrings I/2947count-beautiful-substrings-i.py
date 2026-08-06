class Solution:
    def beautifulSubstrings(self, s: str, k: int) -> int:
        check = {"a", "e", "i", "o", "u"}
        res = 0

        for i in range(len(s)):
            vowels = 0
            consonants = 0
            for j in range(i, len(s)):
                if s[j] in check:
                    vowels += 1
                else:
                    consonants += 1
                if vowels == consonants and vowels * consonants % k == 0:
                    res += 1
        return res     