class UnionFind:
    def __init__(self, n):
        self.parents = {}
        self.heights = {}

        for i in range(n):
            self.parents[i] = i
        
        for i in range(n):
            self.heights[i] = 0
    
    def UnionFind(self, n):
        if self.parents[n] == n:
            return n
        
        return self.UnionFind(self.parents[n])
    
    def merge(self, n1, n2):
        n1_parent = self.UnionFind(n1)
        n2_parent = self.UnionFind(n2)

        if self.heights[n2_parent] > self.heights[n1_parent]:
            self.parents[n1_parent] = n2_parent
        elif self.heights[n1_parent] == self.heights[n2_parent]:
            self.parents[n1_parent] = n2_parent
            self.heights[n2_parent] += 1
        else:
            self.parents[n2_parent] = n1_parent
    
    def get_parents(self):
        parents = [self.UnionFind(i) for i in self.parents]
        return set(parents)

class Solution:
    def minCost(self, n: int, edges: List[List[int]], k: int) -> int:
        edges.sort(key = lambda x : x[2])

        def check_components_count(max_edge_weight):
            union_find = UnionFind(n)

            for n1, n2, w in edges:
                if w > max_edge_weight:
                    break
                
                union_find.merge(n1, n2)
            
            return len(union_find.get_parents())
        
        answer = -1

        weights = [i[2] for i in edges]
        weights.insert(0, 0)

        left, right = 0, len(weights) - 1
        while left <= right:
            mid = (left + right) // 2
            mid_weight = weights[mid]

            components_count = check_components_count(mid_weight)

            if components_count < k:
                answer = mid_weight
                right = mid - 1
            elif components_count == k:
                answer = mid_weight
                right = mid - 1
            else:
                left = mid + 1
            
        return answer