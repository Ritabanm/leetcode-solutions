class Solution:
    def smallestMissingValueSubtree(self, parents, nums):
        n, graph = len(parents), defaultdict(list)

        for i in range(n):
            if parents[i] != -1:
                graph[parents[i]].append(i)

        def function(node):
            for neighbor in graph[node]:
                if nums[neighbor] not in visited:
                    visited.add(nums[neighbor])
                    function(neighbor)

        missing, visited, res, node = 1, set(), [1]*n, -1 

        for i in range(n):
            if nums[i] == 1:
                node = i 
                break 

        if node == -1:
            return res 

        while node != -1:
            visited.add(nums[node])
            function(node)
            while missing in visited:
                missing += 1 
            res[node] = missing 
            node = parents[node]

        return res 