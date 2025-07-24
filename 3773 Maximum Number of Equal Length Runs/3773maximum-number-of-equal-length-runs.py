from collections import Counter

class Solution:
    def maxSameLengthRuns(self, s):
        #Step1: All runs & lengths.
        runs = []
        i = 0
        while i<len(s):
            j = i
            while j<len(s) and s[i]==s[j]:
                j+=1
            runs.append(j-i)
            i = j
        return max(Counter(runs).values())
            