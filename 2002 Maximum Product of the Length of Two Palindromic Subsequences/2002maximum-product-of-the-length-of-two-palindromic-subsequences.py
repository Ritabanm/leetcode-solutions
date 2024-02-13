class Solution:
    def maxProduct(self, s: str) -> int:
        n = len(s)
        palindromes = {}

        def is_palindrome(mask):
            subseq = []
            for i in range(n):
                if mask & (1 << i):
                    subseq.append(s[i])
            return subseq == subseq[::-1]

        for mask in range(1, 1 << n):
            if is_palindrome(mask):
                palindromes[mask] = bin(mask).count('1')

        max_product = 0
        masks = list(palindromes.keys())
        for i in range(len(masks)):
            for j in range(i + 1, len(masks)):
                if masks[i] & masks[j] == 0:
                    max_product = max(max_product, palindromes[masks[i]] * palindromes[masks[j]])

        return max_product