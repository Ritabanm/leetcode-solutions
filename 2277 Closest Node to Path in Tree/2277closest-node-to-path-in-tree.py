class Solution:
    def closestNode(self, n, edges, query):
        graph = defaultdict(list)

        for i,j in edges:
            graph[i].append(j)
            graph[j].append(i)

        def function(start,end):
            stack = [(start,-1,[start])]

            while stack:
                node,parent,path = stack.pop()

                if node == end:
                    return path

                for neighbor in graph[node]:
                    if neighbor != parent:
                        stack.append([neighbor,node,path+[neighbor]])

            return []

        def kunction(node,path):
            stack, visited, path_set = [node], {node}, set(path)

            while stack:
                nd = stack.pop(0)

                if nd in path_set:
                    return nd 

                for neighbor in graph[nd]:
                    if neighbor not in visited:
                        stack.append(neighbor)
                        visited.add(neighbor)

        return [kunction(k,function(i,j)) for i,j,k in query]