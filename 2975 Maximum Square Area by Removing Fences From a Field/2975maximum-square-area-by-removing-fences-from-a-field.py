class Solution:
    def get_edges(self, fences, border):
        points = sorted([1] + fences + [border])

        return {
            points[j]-points[i]
            for i in range(len(points))
            for j in range(i+1, len(points))
        }

    def maximizeSquareArea(self,m,n,hFences,vFences):
        mod = 10**9+7
        h_edges = self.get_edges(hFences, m)
        v_edges = self.get_edges(vFences, n)

        max_edge = max(h_edges & v_edges, default = 0)
        return (max_edge*max_edge)%mod if max_edge else -1