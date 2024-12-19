class LcaBinaryLifting:
    def __init__(self, edges:list[list[int]], s:List[int]):
        n = len(edges)+1
        m = n.bit_length()
        g = [[] for _ in range(n)]
        for x, y in edges:
            g[x].append(y)
            g[y].append(x)
        
        depth = [0]*n
        parent = [[-1]*n for _ in range(m)]
        time_in = [0]*n #dfs timestamp
        time_out = [0]*n
        timer = 0
        path_xor_from_root = [0]*n #the parity of letters from the root
        path_xor_from_root[0] = 1<<s[0]
    
        def dfs(x, fa):
            parent[0][x] = fa
            nonlocal timer
            timer += 1
            time_in[x] = timer
            for y in g[x]:
                if y != fa:
                    depth[y] = depth[x]+1
                    path_xor_from_root[y] = path_xor_from_root[x] ^( 1<<s[y])
                    dfs(y,x)
            time_out[x] = timer
        
        dfs(0, -1)

        for i in range(m-1):
            for x in range(n):
                if parent[i][x] != -1:
                    p = parent[i][x]
                    parent[i+1][x] = parent[i][p]
        self.depth = depth
        self.parent = parent
        self.time_in = time_in
        self.time_out = time_out
        self.path_xor_from_root = path_xor_from_root
    
    def get_kth_ancestor(self, node, k):
        parent = self.parent
        for i in range(k.bit_length()):
            if k>>i & 1:
                node = parent[i][node]
                if node <0:
                    return -1
        
        return node

    def get_lca(self, x, y):
        if self.depth[x] > self.depth[y]:
            x, y = y, x
        y = self.get_kth_ancestor(y, self.depth[y]-self.depth[x])
        if y == x:
            return x
        parent = self.parent
        for i in range(len(parent)-1, -1, -1):
            px, py = parent[i][x], parent[i][y]
            if px != py:
                x, y = px, py
        
        return parent[0][x]    

class Solution:
    def palindromePath(self, n: int, edges: list[list[int]], s: str, queries: list[str]) -> list[bool]:
        tree = [0]*(n+1) #use idx from 1 to n
        def update(i, val):
            while i < len(tree):
                tree[i] ^= val
                i += i & (-i)
        
        def preXor(i):
            res = 0
            while i > 0:
                res ^= tree[i]
                i -= i &(-i)
            
            return res
        
        ord_a = ord('a')
        t = [ord(ch)-ord_a for ch in s]
        g = LcaBinaryLifting(edges, t)
        time_in = g.time_in
        time_out = g.time_out
        path_xor_from_root = g.path_xor_from_root
        ans = []
        for q in queries:
            op, x, y = q.split()
            x = int(x)
            if op[0] == 'u':
                c = ord(y)-ord_a
                val = ( 1<<t[x] ) ^ ( 1<<c )
                t[x] = c
                update(time_in[x], val)
                update(time_out[x]+1, val)
            else:
                y = int(y)
                lca = g.get_lca(x,y)
                res =  path_xor_from_root[x] ^ path_xor_from_root[y] \
                        ^ preXor(time_in[x]) ^ preXor(time_in[y]) \
                        ^ ( 1 << t[lca] )
                ans.append(res & (res-1) == 0)
        
        return ans