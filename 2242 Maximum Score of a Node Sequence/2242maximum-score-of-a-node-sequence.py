class Solution:
    def maximumScore(self, scores: List[int], edges: List[List[int]]) -> int:
        '''
        we want to find the 3 largest connections of each node in each edge
        we can iterate thorough the edges and append the weight of each edge into a
        list of heaps. We only want the 3 largest weighted edges so we will pop
        from the heap if its length is >3
        '''
        n = len(scores)
        top3 = [[] for _ in range(n)]
        for u,v in edges:
            heapq.heappush(top3[u], (scores[v], v))
            heapq.heappush(top3[v], (scores[u], u))
            if len(top3[u])>3:
                heapq.heappop(top3[u])
            if len(top3[v])>3:
                heapq.heappop(top3[v])
        
        res = -1
        for u,v in edges:
            if len(top3[u])<2 or len(top3[v])<2:
                continue
            base = scores[u]+scores[v]
            for sp,p in top3[u]:
                for sq,q in top3[v]:
                    if p!=v and q!=u and p!=q:
                        res = max(res, base+sp+sq)
        return res