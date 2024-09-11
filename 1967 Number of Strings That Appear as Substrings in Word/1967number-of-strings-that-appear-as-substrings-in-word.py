class Solution:
    def numOfStrings(self, patterns, word):
        count = 0
        for item in patterns:
            if item in word:
                count+=1
        return count