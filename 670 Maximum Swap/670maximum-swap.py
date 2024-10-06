class Solution:
    def maximumSwap(self, num: int) -> int:
        # Convert number to a list of characters (digits)
        num_str = list(str(num))

        # Create a dictionary to store the last occurrence of each digit
        last = {int(digit): i for i, digit in enumerate(num_str)}

        # Traverse each digit
        for i, digit in enumerate(num_str):
            # Check if a larger digit exists later in the number
            for d in range(9, int(digit), -1):
                if last.get(d, -1) > i:
                    # Swap the current digit with the larger digit
                    num_str[i], num_str[last[d]] = num_str[last[d]], num_str[i]
                    # Convert back to an integer and return
                    return int(''.join(num_str))

        # If no swap was made, return the original number
        return num
