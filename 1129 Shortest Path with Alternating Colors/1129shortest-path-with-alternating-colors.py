class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        res = [-1] * n
        paths = defaultdict(list)
        
        for r1, r2 in redEdges:
            paths[r1].append((r2, 'r'))
        
        for b1, b2 in blueEdges:
            paths[b1].append((b2, 'b'))
        
        q = deque([(0, 0, '')]) # node, distance, color
        visited = set()
        
        while q:
            node, dist, color = q.popleft()
            
            if (node, color) in visited:  # check if this node has been visited with the same color
                continue
            
            visited.add((node, color))
            
            # update result if this is the first time visiting the node with this color
            if res[node] == -1:
                res[node] = dist
            
            for next_node, next_color in paths[node]:
                if color != next_color:  # make sure we alternate between colors
                    q.append((next_node, dist + 1, next_color))
        
        return res
            