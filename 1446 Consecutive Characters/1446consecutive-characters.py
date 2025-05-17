class Solution:
    def maxPower(self, s):
        count = 0
        maxcount = 0
        prev = None

        for char in s:
            if char==prev:
                count+=1
            else:
                prev=char
                count = 1
            maxcount = max(maxcount, count)
        return maxcount