class Solution:
    def minimumPushes(self, word: str) -> int:
        unique_chars = len(set(word))
        
        if unique_chars <= 8:
            return unique_chars
        elif unique_chars <= 16:
            return 8 + 2 * (unique_chars - 8)
        elif unique_chars <= 24:
            return 8 + 16 + 3 * (unique_chars - 16)
        else:
            return 8 + 16 + 24 + 4 * (unique_chars - 24)  # Handle extra characters