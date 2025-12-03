# sparse binary indexed tree; distinct member, only ins no remove
class sbit:
    def __init__(self, nbit): # num of bit
        self.msb = 1<<(nbit-1)
        self.bound = 1<<nbit
        self.tree = Counter()
        self.member = set() # unique int
    def size(self):
        return len(self.member)
        
    def ins(self,x):
        if x in self.member: return
        self.member.add(x)
        if x == 0: return
        while x < self.bound:
            self.tree[x] += 1
            x += x&(-x)
        return
    
    def combine(self, b):
        for x in b.member:
            self.ins(x)

    def unrank(self,k): #find rank(p) = k, k elements <=p
        if k>len(self.member): return -1
        if 0 in self.member:
            if k == 1: return 0
            k -= 1
        p = 0 # curr position
        jump = self.msb
        while jump: 
            if self.tree[p+jump] < k:
                p += jump
                k -= self.tree[p]
            jump >>= 1
        return p+1
#

class Solution:
    def kthSmallest(self, par: List[int], vals: List[int], queries: List[List[int]]) -> List[int]:
        n,m = len(par),len(queries)
        nbit = len(bin(max(vals))) - 2
        child = [[] for i in range(n)]
        for i in range(1,n):
            child[par[i]].append(i)
        ask = [[] for i in range(n)]
        ans = [0]*m
        for i,(v,k) in enumerate(queries):
            ask[v].append((k,i))
        def dfs(v,curr):
            curr ^= vals[v]
            myset = sbit(nbit)
            myset.ins(curr)
            for u in child[v]:
                p = dfs(u,curr)
                if p.size() > myset.size():
                    p,myset = myset,p
                myset.combine(p)
            for k,i in ask[v]:
                ans[i] = myset.unrank(k)
            return myset
        #
        dfs(0,0)
        return ans