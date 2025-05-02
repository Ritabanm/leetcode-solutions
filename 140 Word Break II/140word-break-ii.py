from typing import List
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)  # Convert list to set for O(1) lookups
        memo = {}  # Memoization dictionary
        
        def backtrack(start):
            if start in memo:
                return memo[start]  # Return cached results
            
            if start == len(s):  
                return [""]  # Base case: end of string
            
            sentences = []
            
            for end in range(start + 1, len(s) + 1):
                word = s[start:end]  # Get substring s[start:end]
                if word in word_set:  # Check if it's a valid word
                    sub_sentences = backtrack(end)  # Recursively solve for rest of the string
                    for sub in sub_sentences:
                        sentences.append(word + (" " + sub if sub else ""))  
            
            memo[start] = sentences  # Cache the result
            return sentences
        
        return backtrack(0)
