class Solution:
    def divisorSubstrings(self, num: int, k: int) -> int:
        num_s = str(num)
        output = 0

        cur = int(num_s[0:k])
        if cur and num%cur==0: output+=1
        for i in range(k,len(num_s)):
            print(cur,i)
            cur = cur%(10**(k-1))
            print(cur)
            cur= cur*10 + int(num_s[i])
            print(cur, 'h')
            if cur and num%cur==0: output+=1
        
        return output
        