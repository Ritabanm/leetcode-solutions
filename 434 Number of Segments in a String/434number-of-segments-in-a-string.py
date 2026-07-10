class Solution:
    def countSegments(self, s):
        segment = 0
        for i in range(len(s)):
            if (i==0 or s[i-1]== ' ') and s[i]!= ' ':
                segment+=1
        return segment