class Solution:
    def shortestPathWithHops(self, n: int, edges: List[List[int]], s: int, d: int, k: int) -> int:
        '''
        dp + shorest path
        '''
        lookup = defaultdict(list)
        for u, v, w in edges:
            lookup[u].append((v, w))
            lookup[v].append((u, w))

        INF = 10 ** 20
        seen = defaultdict(lambda:INF)

        h = []
        heapq.heappush(h, (0, s, k))

        seen[(s, k)] = 0

        while h:
            val, u, k = heapq.heappop(h)
 
            if seen[(u, k)] < val:
                continue

            for v, w in lookup[u]:
                if k:
                    nxt_val = val
                    nxt_k = k - 1

                    if seen[(v, nxt_k)] > nxt_val:
                        
                        seen[(v, nxt_k)] = nxt_val
                        heapq.heappush(h, (nxt_val, v, nxt_k))

                    
                nxt_val = val + w

                if seen[(v, k)] <= nxt_val:
                    continue

                seen[(v, k)] = nxt_val

                heapq.heappush(h, (nxt_val, v, k))



        

        best = 10 ** 10



        for (u, k), val in seen.items():
            if u == d:
                best = min(best, val)

        return best



        



        
        