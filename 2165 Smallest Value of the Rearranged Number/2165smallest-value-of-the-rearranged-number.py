class Solution:
    def smallestNumber(self, num: int) -> int:
        is_negative = num < 0
        digits = list(str(abs(num)))

        if is_negative:
            digits.sort(reverse=True)
        else:
            digits.sort()
            if digits[0] == '0':
                for i in range(1, len(digits)):
                    if digits[i] != '0':
                        digits[0], digits[i] = digits[i], 0
                        break
        
        rearranged_num = int("".join(map(str, digits)))
        return -rearranged_num if is_negative else rearranged_num
        