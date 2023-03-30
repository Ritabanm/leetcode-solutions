class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        # Handle overflow case
        INT_MAX = 2**31 - 1
        INT_MIN = -2**31
        if dividend == INT_MIN and divisor == -1:
            return INT_MAX
        
        # Determine the sign of the result
        negative = (dividend < 0) ^ (divisor < 0)
        
        # Work with absolute values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize quotient
        quotient = 0
        
        # Perform division using subtraction and bit shifting
        while dividend >= divisor:
            temp_divisor, multiple = divisor, 1
            while dividend >= (temp_divisor << 1):
                temp_divisor <<= 1
                multiple <<= 1
            dividend -= temp_divisor
            quotient += multiple
        
        # Apply the sign to the result
        quotient = -quotient if negative else quotient
        
        # Ensure the result is within bounds
        return max(min(quotient, INT_MAX), INT_MIN)
