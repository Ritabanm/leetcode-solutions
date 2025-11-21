class Solution:
    def kthPalindrome(self, queries: List[int], intLength: int) -> List[int]:
        half_length = (intLength + 1) // 2
        start = 10 ** (half_length - 1)
        end = 10 ** half_length - 1

        result = []
        for q in queries:
            half_number = start + q - 1
            if half_number > end:
                result.append(-1)
            else:
                second_half = str(half_number)[:-1] if intLength % 2 else str(half_number)
                result.append(int(str(half_number) + second_half[::-1]))

        return result