class Solution:
    def addMinimum(self, word: str) -> int:
        
        target = "abc"
        i, j = 0, 0
        count = 0

        while i < len(word):
            if j == len(target):
                j = 0
            if word[i] == target[j]:            
                i += 1
                j += 1
            else:         
                count += 1
                j += 1
    
        count += len(target) - j
        return count