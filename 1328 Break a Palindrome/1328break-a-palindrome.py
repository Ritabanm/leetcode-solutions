class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        pal = list(palindrome)
        if len(pal)==1:
            return ""
        
        for c in range(len(pal)//2):
            if pal[c]!='a':
                pal[c]='a'
                return "".join(pal)
        pal[-1] = 'b'
        return "".join(pal
        )