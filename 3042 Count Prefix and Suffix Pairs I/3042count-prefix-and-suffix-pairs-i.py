from typing import List

class Solution:
    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        def isPrefixAndSuffix(str1: str, str2: str) -> bool:
            """Helper function to check if str1 is both a prefix and a suffix of str2."""
            return str2.startswith(str1) and str2.endswith(str1)

        count = 0
        n = len(words)
        for i in range(n):
            for j in range(i + 1, n):
                if isPrefixAndSuffix(words[i], words[j]):
                    count += 1
        return count