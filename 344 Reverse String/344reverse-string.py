"""class Solution:
    def reverseString(self, s):
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left, right = left + 1, right - 1"""

class Solution:
    def reverseString(self, s):
        l,r = 0, len(s)-1
        while l<r:
            s[l], s[r] = s[r], s[l]
            l,r = l+1, r-1