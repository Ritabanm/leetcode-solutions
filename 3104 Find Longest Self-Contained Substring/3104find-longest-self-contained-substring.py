class Solution:
    def maxSubstringLength(self, s: str) -> int:
        # Store first and last occurrence of each character
        occurrences = {}
        for index, ch in enumerate(s):
            if ch not in occurrences:
                occurrences[ch] = [index, index]  # [first_occurrence, last_occurrence]
            occurrences[ch][1] = index  # Update last occurrence

        max_length = -1  # Default value if no valid substring is found

        for ch, (first, last) in occurrences.items():
            max_end = last  # Track the farthest extension of the substring
            for index in range(first, len(s)):
                end_char = s[index]
                
                # If a character appears before 'first', it's not a valid substring
                if occurrences[end_char][0] < first:
                    break
                
                # Extend max_end to include this character
                max_end = max(max_end, occurrences[end_char][1])

                # Check if a valid substring is formed
                if max_end == index and max_end - first + 1 != len(s):
                    max_length = max(max_length, max_end - first + 1)

        return max_length


                    

        





        

                    

        





        