class Solution:
    def makePalindrome(self, s: str) -> bool:
        count = 0
        p1 = 0
        p2 = len(s)-1

        while p1<p2:
            if s[p1]!=s[p2]:
                count+=1
                if count>2:
                    return False
            
            p1+=1
            p2-=1
        return True