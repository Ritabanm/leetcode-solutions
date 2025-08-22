from collections import Counter
class Solution:
    def largestPalindromic(self, num: str) -> str:
        freq = Counter(num)
        first_half = []
        middle = ""

        for digit in range(9,-1,-1):
            digit_char = str(digit)
            if digit_char in freq:

                digit_count = freq[digit_char]
                num_pairs = digit_count // 2

                if num_pairs:
                    if not first_half and not digit:
                        freq["0"] = 1
                    else:
                        first_half.append(digit_char * num_pairs)
                
                if digit_count % 2 and not middle:
                    middle = digit_char
        
        if not middle and not first_half:
            return "0"
        
        return "".join(first_half + [middle] + first_half[::-1])
        