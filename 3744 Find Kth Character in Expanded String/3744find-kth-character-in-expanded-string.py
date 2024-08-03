class Solution:
    def kthCharacter(self, s: str, k: int) -> str:

        words = s.replace(' ', '| |').split('|')
        
        for word in words:
            n = len(word)
            length = (n * (n + 1)) // 2
            
            if k < length:
                lastWd = word
                break
            
            k -= length

        i = 1

        while i <= k:
            k -= i
            i += 1

        return lastWd[i - 1]