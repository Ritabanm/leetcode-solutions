class Solution:

    def getSum(self, a: int, b: int) -> int:
        # 32-bit mask in hexadecimal is 0xFFFFFFFF
        mask = 0xFFFFFFFF
        # We use 32-bit integers, so we need to handle overflow
        while b != 0:
            # Calculate the sum without carry
            sum_without_carry = (a ^ b) & mask
            # Calculate the carry
            carry = ((a & b) << 1) & mask
            # Update a and b for the next iteration
            a, b = sum_without_carry, carry
        # Handle overflow for negative numbers in 32-bit representation
        return a if a <= 0x7FFFFFFF else ~(a ^ mask)