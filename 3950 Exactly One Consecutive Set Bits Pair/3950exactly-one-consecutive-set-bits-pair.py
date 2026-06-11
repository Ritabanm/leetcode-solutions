class Solution:
    def consecutiveSetBits(self, n: int) -> bool:
        count = 0
        s = bin(n)[2:]
        for i in range(len(s)-1):
            if(s[i]=="1" and s[i+1]=="1"):
                count+=1
        return count ==1