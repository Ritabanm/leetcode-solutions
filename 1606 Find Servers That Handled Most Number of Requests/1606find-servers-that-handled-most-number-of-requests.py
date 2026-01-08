class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        count  = [0]*k
        busy, free =[], SortedList(list(range(k)))
        for i, start in enumerate(arrival):
            while busy and busy[0][0]<=start:
                _, server_id = heapq.heappop(busy)
                free.add(server_id)
            if free:
                index = free.bisect_left(i%k)
                busy_id = free[index] if index<len(free) else free[0]
                free.remove(busy_id)
                heapq.heappush(busy, (start+load[i],busy_id))
                count[busy_id]+=1
        max_job = max(count)
        return [i for i,n in enumerate(count) if n==max_job]