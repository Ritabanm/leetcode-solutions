from collections import Counter
from typing import List

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        # Create a frequency count for the characters in chars
        chars_count = Counter(chars)
        total_length = 0
        
        # Loop through each word in words
        for word in words:
            # Create a frequency count for the characters in the current word
            word_count = Counter(word)
            
            # Check if all characters in the word can be formed using chars
            can_form = True
            for char in word_count:
                if word_count[char] > chars_count.get(char, 0):
                    can_form = False
                    break
            
            # If the word can be formed, add its length to the total length
            if can_form:
                total_length += len(word)
        
        return total_length
