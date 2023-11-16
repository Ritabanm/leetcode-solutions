class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # Convert each character in the string 'p' to its corresponding index in the alphabet
        alphabet_indices = list(map(lambda x: ord(x) - ord('a'), p))

        # Dictionary to store the maximum length of substrings ending with each letter
        max_substring_lengths = {i: 0 for i in range(26)}
        
        start, run_length, last_char_index = alphabet_indices[0], 1, alphabet_indices[0]
        
        # Function to update the max_substring_lengths dictionary
        def update_runs():
            nonlocal start, run_length, last_char_index
            for _ in range(27):
                if max_substring_lengths[start] < run_length:
                    max_substring_lengths[start] = run_length
                start, run_length = (start + 1) % 26, run_length - 1
                if run_length <= 0:
                    break

        # Iterate through the alphabet indices to calculate run lengths
        for current_index in alphabet_indices[1:]:
            if current_index == last_char_index + 1 or (last_char_index == 25 and current_index == 0):
                run_length += 1
            else:
                update_runs()
                start, run_length, last_char_index = current_index, 1, current_index
            last_char_index = current_index
        update_runs()

        # Sum the lengths of all valid substrings
        total_unique_substrings = sum(max_substring_lengths.values())
        return total_unique_substrings