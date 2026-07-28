class Solution:
    def canMakePaliQueries(self, s: str, queries: List[List[int]]) -> List[bool]:
        l = len(s)
        mem = [0] * (l+1)
        mask = 0
        for i in range(l):
            idx = ord(s[i]) - ord('a')
            mask ^= 1 << idx
            mem[i+1] = mask
        
        ans = [False] * len(queries)
        for i in range(len(queries)):
            left,right,k = queries[i]
            chars = mem[right+1] ^ mem[left]
            for j in range(k):
                if chars == 0:
                    break
                chars &= (chars-1)
                chars &= (chars-1)
            chars &= (chars-1)
            if chars == 0:
                ans[i] = True
        
        return ans