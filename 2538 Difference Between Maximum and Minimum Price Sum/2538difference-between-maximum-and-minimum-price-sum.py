class Solution:
    def maxOutput(self, n: int, edges: List[List[int]], price: List[int]) -> int:
        E=edges;P=price
        adj=[[] for _ in range(n)]
        for u,v in E:
            adj[u].append(v)
            adj[v].append(u)
        res=[0]
        def dfs(node,par):
            mxWLeaf=P[node];mxWOLeaf=0
            for nei in adj[node]:
                if nei==par: continue
                neiWLeaf,neiWOLeaf=dfs(nei,node)
                res[0]=max(res[0],mxWLeaf+neiWOLeaf,mxWOLeaf+neiWLeaf)
                mxWLeaf=max(mxWLeaf,P[node]+neiWLeaf)
                mxWOLeaf=max(mxWOLeaf,P[node]+neiWOLeaf) # leaf as nei then nei of nei.... leaf
            return mxWLeaf,mxWOLeaf
        dfs(0,-1)
        return res[0]