class Solution:
    def isPalindromic(self, s: str) -> bool:
        binary_str = "".join(bin(ord(c))[2:].zfill(8) for c in s)
        return binary_str == binary_str[::-1]