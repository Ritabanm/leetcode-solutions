def get_distance(a, b):
    r1, c1 = divmod(ord(a) - ord('A'), 6)
    r2, c2 = divmod(ord(b) - ord('A'), 6)
    return abs(r1 - r2) + abs(c1 - c2)

class Solution:
    def minimumDistance(self, word: str) -> int:
        previous = word[0]
        cost = [0] * 26
        for letter in word:
            prev_cur = get_distance(letter, previous)
            small = float('inf')
            for i, val in enumerate(cost):
                cost[i] += prev_cur
                dist = get_distance(letter, chr(i + ord('A')))
                small = min(small, val+dist)
            
            idx = ord(previous) - ord('A')
            cost[idx] = min(cost[idx], small)
            previous = letter
        return min(cost)