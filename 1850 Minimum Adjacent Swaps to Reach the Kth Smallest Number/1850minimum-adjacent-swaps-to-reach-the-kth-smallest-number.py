class Solution:
    def getMinSwaps(self, num: str, k: int) -> int:
 
        n, num = len(num), list(map(int,num))               # <-- 1)
        perm = num[::]
 
        for _ in range(k):                                  # <-- 2)
            
            i = n - 1
            while i > 0 and perm[i-1] >= perm[i]: i -= 1
             
            if i > 0:    
                j = n - 1
                while perm[j] <= perm[i-1]:  j -= 1
                perm[i-1], perm[j] = perm[j], perm[i-1]
            perm[i:] = perm[n-1:i-1:-1]

        i = res = 0                                         # <-- 3)
        while i < n:
            j = i
            while perm[j] != num[i]: j += 1
            
            while i < j:
                perm[j-1], perm[j] = perm[j], perm[j-1]
                j -= 1
                res += 1
            
            i+= 1
        
        return res                                          # <-- 4)