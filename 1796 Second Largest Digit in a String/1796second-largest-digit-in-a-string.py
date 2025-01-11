class Solution:
    def secondHighest(self, s: str) -> int:
        digits = set()
        for ch in s:
            if ch.isdigit():
                digits.add(int(ch))
       
        if len(digits)<2:
            return -1

        sorted_digits = sorted(digits, reverse = True)
        return sorted_digits[1]

