class Solution:
    def greatestLetter(self, s: str) -> str:
        letter_set = set(s)  # Store all characters in a set

        for char in reversed("ABCDEFGHIJKLMNOPQRSTUVWXYZ"):
            if char in letter_set and char.lower() in letter_set: 
                return char  
        return ""