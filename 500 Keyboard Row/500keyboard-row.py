from typing import List

class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        row1 = ['q','w','e','r','t','y','u','i','o','p']
        row2 = ['a','s','d','f','g','h','j','k','l']
        row3 = ['z','x','c','v','b','n','m']
        
        ans = []
        for word in words:
            lower_word = word.lower()
            if all(char in row1 for char in lower_word) or \
               all(char in row2 for char in lower_word) or \
               all(char in row3 for char in lower_word):
                ans.append(word)  # Append the original word (with case)
        return ans