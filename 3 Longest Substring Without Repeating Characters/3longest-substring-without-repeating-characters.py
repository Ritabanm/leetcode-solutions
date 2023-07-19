"""class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = [None]*128

        left = 0
        right= 0
        res = 0
        
        while right<len(s):
            r = s[right]
            index = chars[ord(r)]

            if index is not None and left<=index<right:
                left = index+1
            
            res = max(res, right-left+1)
            chars[ord(r)] = right
            right+=1
        return res"""

class Solution:
    def lengthOfLongestSubstring(self, s):
        chars = [None]*128
        left = 0
        right = 0
        res = 0
        while right<len(s):
            r = s[right]
            index = chars[ord(r)]
            if index is not None and left<=index<=right:
                left = index+1
            res = max(res, right-left+1)
            chars[ord(r)] = right
            right+=1
        return res