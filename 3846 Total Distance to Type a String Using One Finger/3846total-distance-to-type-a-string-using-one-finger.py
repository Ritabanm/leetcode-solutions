class Solution:
    def totalDistance(self, s: str) -> int:
        keyboard = ['qwertyuiop', 'asdfghjkl', 'zxcvbnm']
        key_pos = dict()
        for i in range(len(keyboard)):
            for j in range(len(keyboard[i])):
                key_pos[keyboard[i][j]] = (i, j)
        curr_i, curr_j = key_pos['a']
        res = 0
        for c in s:
            res += abs(key_pos[c][0] - curr_i) + abs(key_pos[c][1] - curr_j)
            curr_i, curr_j = key_pos[c]
        return res