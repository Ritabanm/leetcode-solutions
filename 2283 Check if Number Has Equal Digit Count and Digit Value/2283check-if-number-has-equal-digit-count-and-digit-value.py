from collections import Counter

class Solution:
    def digitCount(self, num: str) -> bool:
        freq = Counter(num)
        n = len(num)
        for i in range(n):
            if int(num[i]) != freq[str(i)]:
                return False
        return True