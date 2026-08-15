from collections import defaultdict, deque

class Solution:
    def weightedSum(self, parent: list[int], nums: list[int]) -> int:
        n = len(parent)
        adj = defaultdict(list)
        for i in range(1, n):
            adj[parent[i]].append(i)
            
        depth = [0] * n
        queue = deque([0])
        depth[0] = 1
        max_depth = 1
        
        while queue:
            curr = queue.popleft()
            for neighbor in adj[curr]:
                depth[neighbor] = depth[curr] + 1
                max_depth = max(max_depth, depth[neighbor])
                queue.append(neighbor)
                
        total_weight = 0
        for i in range(n):
            total_weight += nums[i] * (max_depth - depth[i] + 1)
            
        return total_weight