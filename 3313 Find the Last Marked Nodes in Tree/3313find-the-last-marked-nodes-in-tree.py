class Solution:
    def lastMarkedNodes(self, edges: List[List[int]]) -> List[int]:
        tree = [[] for _ in range(len(edges) + 1)]
        for e in edges:
            tree[e[0]].append(e[1])
            tree[e[1]].append(e[0])

        def furthest(node):
            seen = [False for _ in range(len(tree))]
            seen[node] = True
            stack = [(node, 0)]
            max_steps = 0
            max_node = node
            
            while stack:
                n, steps = stack.pop(-1)
                if steps >  max_steps:
                    max_node = n
                    max_steps = steps
                for nei in tree[n]:
                    if not seen[nei]:
                        seen[nei] = True
                        stack.append((nei, steps + 1))
            return max_node
        
        furthest_1 = furthest(0)
        furthest_2 = furthest(furthest_1)
        
        def get_distance(node):
            seen = [False for _ in range(len(tree))]
            seen[node] = True
            stack = [(node, 0)]
            distance = [None for _ in range(len(tree))]

            while stack:
                n, steps = stack.pop(-1)
                distance[n] = steps
                for nei in tree[n]:
                    if not seen[nei]:
                        seen[nei] = True
                        stack.append((nei, steps + 1))
            return distance
        
        furthest_1_distance = get_distance(furthest_1)
        furthest_2_distance = get_distance(furthest_2)
        
        result = []
        for i in range(len(tree)):
            if furthest_1_distance[i] > furthest_2_distance[i]:
                result.append(furthest_1)
            else: result.append(furthest_2)
        return result