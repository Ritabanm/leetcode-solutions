class Solution:
    def findSubstring(self, s, words):
        if not s or not words:
            return []

        word_length = len(words[0])  # Length of each word in the list
        total_length = len(words) * word_length  # Total length of concatenated words
        words_count = {}  # Dictionary to store the count of each word
        result = []  # List to store the starting indices of valid substrings

        # Count the occurrences of each word in the list
        for word in words:
            if word in words_count:
                words_count[word] += 1
            else:
                words_count[word] = 1

        # Iterate through possible starting indices within a word length
        for i in range(word_length):
            left, right = i, i  # Initialize left and right pointers
            current_count = {}  # Dictionary to track word counts in the current window
            count = 0  # Counter for valid word matches

            # Slide the window through the string
            while right + word_length <= len(s):
                word = s[right:right + word_length]  # Extract the current word
                right += word_length  # Move the right pointer

                if word in words_count:  # Check if the current word is in the words list
                    if word in current_count:
                        current_count[word] += 1
                    else:
                        current_count[word] = 1

                    count += 1  # Increment the word count in the current window

                    # Adjust the window by removing words until it's valid
                    while current_count[word] > words_count[word]:
                        removed_word = s[left:left + word_length]  # Extract the leftmost word
                        left += word_length  # Move the left pointer
                        current_count[removed_word] -= 1
                        count -= 1

                    if count == len(words):  # If all words are found, add the starting index to the result
                        result.append(left)

                else:
                    current_count.clear()  # Clear the current word counts
                    count = 0
                    left = right  # Reset pointers to the next position

        return result  # Return the list of starting indices

# Testing the function usage
s = "barfoothefoobarman"
words = ["foo","bar"]
solution = Solution()
result = solution.findSubstring(s, words)
print("String: ", s)
print("Words:", words)
print(result)  # Output: [0, 9]
