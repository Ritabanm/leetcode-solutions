class Solution:
    def minOperations(self, s: str) -> int:

        for idx in range(25):
            if ascii_lowercase[1:][idx] in s:
                return 25 - idx

        return 0