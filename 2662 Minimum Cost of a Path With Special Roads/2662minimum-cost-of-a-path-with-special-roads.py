class Solution:
    def minimumCost(self, start: List[int], target: List[int], specialRoads: List[List[int]]) -> int:
        mp = defaultdict(list, {tuple(target) : [(0, 0, 0)]})
        for x, y, xx, yy, cost in specialRoads: 
            mp[x, y].append((xx, yy, cost))
        dist = defaultdict(lambda : inf)
        dist[tuple(start)] = 0 
        pq = [(0, *start)]
        while pq: 
            d, x, y = heappop(pq)
            if [x, y] == target: return d 
            for xx, yy, cost in mp[x, y]: 
                if d+cost < dist[xx, yy]: 
                    dist[xx, yy] = d+cost
                    heappush(pq, (d+cost, xx, yy))
            for x1, y1 in mp: 
                dd = d + abs(x1-x) + abs(y1-y)
                if dd < dist[x1, y1]: 
                    dist[x1, y1] = dd
                    heappush(pq, (dd, x1, y1))