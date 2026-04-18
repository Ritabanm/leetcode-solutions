class Solution:
    def calculate(self, s: str) -> int:
        stack = []      # Stack to handle signs for parentheses
        result = 0
        num = 0          # Variable to build numbers from digits
        sign = 1         # Current sign
        
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)  # Build numbers from digits
            elif char == "+":
                result += sign * num        # Add the current number to result
                num = 0                     # Reset num for next number
                sign = 1                    # Update sign to positive
            elif char == "-":
                result += sign * num        # Add the current number to result
                num = 0                     # Reset num for next number
                sign = -1                   # Update sign to negative
            elif char == "(":
                stack.append(result)        # Push result onto stack
                stack.append(sign)          # Push sign onto stack
                result = 0                  # Reset result for subexpression
                sign = 1                    # Reset sign to positive
            elif char == ")":
                result += sign * num        # Add the last number to result
                result *= stack.pop()       # Multiply by the sign from the stack
                result += stack.pop()       # Add the previous result from the stack
                num = 0                     # Reset num for next number
        
        result += sign * num                # Add the final number to result
        
        return result
