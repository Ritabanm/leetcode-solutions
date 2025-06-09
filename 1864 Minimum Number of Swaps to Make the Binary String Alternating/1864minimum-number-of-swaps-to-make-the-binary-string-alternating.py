class Solution:
    def minSwaps(self, s: str) -> int:
        count_0 = s.count("0")
        count_1 = len(s) - count_0

        if abs(count_0 - count_1) > 1:
            return -1

        def count_swaps(start_char):
            swaps = 0

            for c in s:
                if c != start_char:
                    swaps += 1
                start_char = "1" if start_char == "0" else "0"
            return swaps // 2

        swap_startChar_0 = count_swaps("0")
        swap_startChar_1 = count_swaps("1")

        if len(s) % 2 == 0:
            return min(swap_startChar_0, swap_startChar_1)
        
        return swap_startChar_0 if count_0>count_1 else swap_startChar_1