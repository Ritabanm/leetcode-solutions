class Solution:
    def stringShift(self, s: str, shift: List[List[int]]) -> str:
        left_shift=0
        for direction, amount in shift:
            if direction ==1:
                amount = -amount
            left_shift += amount
        left_shift%=len(s)
        s = s[left_shift:] + s[:left_shift]
        return s