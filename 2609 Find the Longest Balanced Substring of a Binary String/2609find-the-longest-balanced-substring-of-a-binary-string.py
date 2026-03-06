class Solution:
    def findTheLongestBalancedSubstring(self, s: str) -> int:
        i =0
        k = len(s)//2
        while i<k:
            j = (i+k)//2
            if ('0'*j + '1'*j) in s:
                i =j
                if i==k-1:
                    if ('0'*k + '1'*k) in s:
                        i = k
                    break
            else:
                k = j-1
        return i*2