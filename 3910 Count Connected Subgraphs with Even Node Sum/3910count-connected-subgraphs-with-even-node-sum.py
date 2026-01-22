class Solution:
    def evenSumSubgraphs(self, nums: list[int], edges: list[list[int]]) -> int:
        
        adjList = defaultdict(list)

        for e1,e2 in edges:
            adjList[e1].append(e2)
            adjList[e2].append(e1)

        res = []
        
        def dfs(i, temp):

            if i == len(nums):
                return

            for j in range(i,len(nums)):
                # take
                temp.append(j)
                res.append(temp[:])
                dfs(j+1,temp)
                # not take
                temp.pop()

        dfs(0,[])

        def check(n,visited, nodes):
            visited.add(n)
            for nei in adjList[n]:
                #No ned to traverse the entire graph, keep the traversal limited
                if nei in nodes and nei not in visited:                    
                    check(nei,visited,nodes)
            
        count = 0
        for num in res:
            sums = 0
            edge = True
            visited = set()
            
            for i in num:
                sums += nums[i]
 
            check(num[0], visited, set(num))

            if len(visited) != len(num):
                continue
            if sums%2 != 0:
                continue
    
            else:
                count += 1
        
        return count
                 
            