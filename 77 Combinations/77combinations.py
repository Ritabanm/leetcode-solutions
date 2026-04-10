class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        def bt(s,c):
            if len(c)==k:
                res.append(c[:])
                return 
            for i in range(s,n+1):
                c.append(i)
                bt(i+1,c)
                c.pop()
        bt(1,[])
        return res