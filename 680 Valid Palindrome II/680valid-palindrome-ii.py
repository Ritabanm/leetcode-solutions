class Solution(object):
    def validPalindrome(self,s):
        l = 0
        r = len(s)-1

        while l<r:
            if s[l]!=s[r]:
                one =s[l:r]
                two = s[l+1:r+1]
                return one==one[::-1] or two==two[::-1]
            l+=1
            r-=1
        return True