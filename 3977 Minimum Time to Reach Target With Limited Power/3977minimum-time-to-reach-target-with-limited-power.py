class Solution:
    def minTimeMaxPower(self, n, edges, power, cost, source, target):
        graph = defaultdict(list)

        for u,v,t in edges:
            graph[u].append([v,t])

        dict1 = defaultdict(list)

        for i in range(n):
            for p in range(power+1):
                dict1[(i,p)] = float("inf")

        
        dict1[(source,power)] = 0

        stack = [(0,-power,source,power)]

        while stack:
            t,np,s,p = heapq.heappop(stack)

            if s == target:
                return [t,p]

            for neighbor,time in graph[s]:
                if p-cost[s] >= 0 and dict1[(neighbor,p-cost[s])] > t+time:
                    dict1[(neighbor,p-cost[s])] = t+time
                    heapq.heappush(stack,(t+time,-(p-cost[s]),neighbor,p-cost[s]))

        return [-1,-1]