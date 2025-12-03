class UnionFind:

    def __init__(self, N):
        self.count = N              
        self.parent = [i for i in range(N)]
        self.rank = [1] * N
        
        
    def find(self, p):
        if p != self.parent[p]:
            self.parent[p] = self.find(self.parent[p]) 
        return self.parent[p]

    def union(self, p, q):
        prt, qrt = self.find(p), self.find(q)
        if prt == qrt: return False
        if self.rank[prt] >= self.rank[qrt]: 
            self.parent[qrt] = prt
            self.rank[prt] += self.rank[qrt]
        else:
            self.parent[prt] = qrt
            self.rank[qrt] += self.rank[prt]
            
        self.count -= 1 
        return True 
	    

class Solution:
    def minRunesToAdd(self, n: int, crystals: List[int], flowFrom: List[int], flowTo: List[int]) -> int:
        '''
        min edges to add s.t. all receive at least one crystal


        union find?


        or dfs from every crytsal if its not in seen

        union find remaining components

        then UF.count is ans
        '''
        seen = [0]*n

        lookup = defaultdict(set)

        for u, v in zip(flowFrom,flowTo):
            lookup[u].add(v)


        def dfs(u):

            for v in lookup[u]:
                if not seen[v]:
                    seen[v]=1
                    dfs(v)

        for u in crystals:
            if not seen[u]:
                seen[u]=1
                dfs(u)
        
      
        A = []
        for index, x in enumerate(seen):
            if x==0:
                A.append(index)


        if not A:
            return 0

        A = set(A)

        # print(A)


        for x in A:
            
            for u in list(lookup[x]):
                if u not in A:
                    lookup[x].remove(u)


        # print(lookup)

        inward = defaultdict(int)

        total = 0

        for x in A:
            for v in lookup[x]:
                
                inward[v]+=1



        '''
        add nodes with no inward edge?

        then cycles
        '''

        def dfs2(u):
            marked.add(u)

            for v in lookup[u]:
                if v not in marked:
                    marked.add(v)
                    dfs2(v)


        total = 0

        marked = set()

       

        for x in list(A):
            if inward[x]==0:
                total += 1
                dfs2(x)


        for v in marked:
            A.remove(v)


        if not A:
            return total

        
        A = list(A)
        
        mp = defaultdict(int)

        for index, x in enumerate(A):
            mp[x]=index

        UF = UnionFind(len(A))


        A = set(A)

        


        seen = set()

       

       

        def dfs3(u):
            for v in lookup[u]:
                if v not in A:
                    continue

                UF.union(mp[u],mp[v])
        
                if v not in seen:
                    seen.add(v)
                    dfs3(v)


        for x in A:
            if x not in seen:
                seen.add(x)
                dfs3(x)


        return UF.count+total