class Solution:

    def mirrorFrequency(self, s: str) -> int:
  
        ans = 0
        d = Counter(s)                          # <-- 1)

        for i in range(13):                     # <-- 2)
            ans+= abs(d[ascii_lowercase[i]] - d[ascii_lowercase[~i]])
            
        for i in range( 5):                     # <-- 3) 
            ans+= abs(d[digits[i]] - d[digits[~i]])

        return ans                              # <-- 4)
        