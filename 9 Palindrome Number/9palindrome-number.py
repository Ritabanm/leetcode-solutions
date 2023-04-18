class Solution:
    def isPalindrome(self, x):
        if x<0 or (x%10==0 and x!=0):
            return False
        revN = 0
        while x>revN:
            revN = revN*10+x%10
            x//=10
        return x==revN or x==revN//10
