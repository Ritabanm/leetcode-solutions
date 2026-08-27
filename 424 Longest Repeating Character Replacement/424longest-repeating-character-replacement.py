class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left_pointer = 0
        max_frequency = 0
        max_length = 0
        char_frequency = Counter()

        for right_pointer, char in enumerate(s):
            char_frequency[char] += 1
            max_frequency = max(max_frequency, char_frequency[char])

            # Check if the current window size minus the count of the most frequent character is greater than k
            if (right_pointer - left_pointer + 1) - max_frequency > k:
                # Shrink the window from the left
                char_frequency[s[left_pointer]] -= 1
                left_pointer += 1

            # Update the maximum length of the window
            max_length = max(max_length, right_pointer - left_pointer + 1)

        return max_length