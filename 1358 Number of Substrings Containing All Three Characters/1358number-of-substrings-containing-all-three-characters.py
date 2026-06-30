class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        freq = [0] * 3
        res = 0
        
        left = 0
        for right in range(n):
            char = s[right]
            if char == 'a':
                freq[0] += 1
            elif char == 'b':
                freq[1] += 1
            elif char == 'c':
                freq[2] += 1
            
            while freq[0] > 0 and freq[1] > 0 and freq[2] > 0:
                char = s[left]
                
                if char == 'a':
                    freq[0] -= 1
                elif char == 'b':
                    freq[1] -= 1
                elif char == 'c':
                    freq[2] -= 1
                
                res += n - right
                left += 1
        
        return res