class Solution:
    def percentageLetter(self,s,letter):
        count = 0
        for item in s:
            if item==letter:
                count+=1
        total_length = len(s)
        return int((count/total_length)*100)