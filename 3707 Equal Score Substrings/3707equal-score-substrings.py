class Solution:
    def scoreBalance(self, s: str) -> bool:
        total_sum = sum(map(ord, s)) - ord('a') * len(s) + len(s)
        left_sum = 0
        for w in s:
            left_sum += ord(w) - ord('a') + 1
            if left_sum == total_sum - left_sum:
                return True
        return False