class Solution:
    def checkContradictions(self, equations, values):
        n, dict1, graph = len(equations), {}, defaultdict(set)

        def find(x):
            if x not in dict1:
                return x 
            else:
                if x != dict1[x]:
                    dict1[x] = find(dict1[x])
                return dict1[x]

        def union(x,y):
            a,b = find(x),find(y)

            if a != b:
                dict1[b] = a

        def function(start,end):
            stack, visited = [(start,1)], {start}

            while stack:
                node,val = stack.pop(0)

                if node == end:
                    return val 

                for neighbor,v in graph[node]:
                    if neighbor not in visited:
                        stack.append((neighbor,v*val))
                        visited.add(neighbor)

            return -1
        
        for i in range(n):
            if find(equations[i][0]) != find(equations[i][1]):
                graph[equations[i][0]].add((equations[i][1],values[i]))
                graph[equations[i][1]].add((equations[i][0],1/values[i]))
                union(equations[i][0],equations[i][1])
            else:
                if function(equations[i][0],equations[i][1]) != values[i]:
                    return True

        return False 