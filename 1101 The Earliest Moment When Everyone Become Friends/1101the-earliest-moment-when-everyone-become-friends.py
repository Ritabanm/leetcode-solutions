class Solution:
    def earliestAcq(self, logs: List[List[int]], n: int) -> int:
        #Dijkstra's algorithm 
        # Time O(ElogN)
        # Space O(V+E)
        graph = collections.defaultdict(list) 
        min_time, min_node = math.inf, None 
        for e in logs: 
            graph[e[1]].append((e[0], e[2]))
            graph[e[2]].append((e[0], e[1]))
            if e[0] < min_time: 
                min_time = e[0] 
                min_node = e[1] 

        timestamp_arr = [math.inf] * n
        timestamp_arr[min_node] = min_time 
        visited_set = set()
        pq = [(min_time, min_node)] 

        res = min_time
        while pq: 
            time, node = heapq.heappop(pq) 
            if node in visited_set: continue 
            visited_set.add(node) 
            res = max(res, time)
            if len(visited_set) == n: return res

            for (cost, cur_node) in graph[node]:
                if cost < timestamp_arr[cur_node]: 
                    timestamp_arr[cur_node] = cost 
                    heapq.heappush(pq, (cost, cur_node))
        return -1







