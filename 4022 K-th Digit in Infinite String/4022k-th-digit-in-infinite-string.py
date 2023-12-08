class Solution:
    def kthDigit(self, k: int) -> int:
        if k < 10:
            return k

        d = 1

        while k > 9 * (10 ** (d - 1)) * d:
            k -= 9 * (10 ** (d - 1)) * d
            d += 1

        block_index = (k - 1) // (10 * d)
        pos = (k - 1) % (10 * d)

        b = 10 ** (d - 2) + block_index

        number_index = pos // d
        digit_index = pos % d

        if b % 2 == 1:
            number_index = 9 - number_index

        number = 10 * b + number_index

        return int(str(number)[digit_index])