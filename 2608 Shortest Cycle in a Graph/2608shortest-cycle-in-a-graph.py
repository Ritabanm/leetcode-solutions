class Solution:
    def findShortestCycle(self, n: int, edges: List[List[int]]) -> int:
        
        def bfs(source):

            nonlocal ans 

            q = [(source, 0)]
            v = {source:0}
            par = {source: -1}
            #print('source is ', source)
            
            

            while q:

                i, dist = q.pop(0)
                #print(i,dist)

                if dist>=ans:break 

                
                for j in x[i]:
                    if j not in v:
                        v[j] = dist+1
                        par[j] = i
                        q.append((j,dist+1))
                    elif j!=par[i]:
                        ans = min(ans, v[j]+v[i]+1)

            

        x = [[] for i in range(n)]

        for i,j in edges:
            x[i].append(j)
            x[j].append(i)
    
        ans = inf
        for i in range(n):
            bfs(i)

        return -1 if ans == inf else ans 
