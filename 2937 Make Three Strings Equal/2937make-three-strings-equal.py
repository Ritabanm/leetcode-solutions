class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
          
        s1= list(s1)
        s2 = list(s2)
        s3 = list(s3)
        
        sl = min(len(s1),len(s2), len(s3))
        count=0

        for i in range(sl):
            if s1[i] == s2[i] == s3[i]:
                count+=1
            else:
                break

        if count == 0: return -1

        return len(s1)+len(s2)+len(s3) - 3*count     
                