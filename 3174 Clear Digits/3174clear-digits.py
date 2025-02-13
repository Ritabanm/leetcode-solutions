class Solution:
    def clearDigits(self, s: str) -> str:
        result = list(s)  # Convert the string to a list (mutable)
        nums = "0123456789"  # Represent digits as strings for comparison
        i = 0  # Start index
        
        while i < len(result):  # Iterate over the string
            if result[i] in nums:  # If the current character is a digit
                # Find and remove the closest non-digit character to the left
                if i > 0:  # Ensure there is a character to the left
                    result.pop(i - 1)  # Remove the left non-digit character
                    i -= 1  # Adjust the index after removal
                
                # Remove the digit itself
                result.pop(i)
            else:
                i += 1  # Move to the next character
        
        return ''.join(result)