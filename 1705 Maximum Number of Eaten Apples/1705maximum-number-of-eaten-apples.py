import heapq

class Solution:
    def eatenApples(self, apples, days):
        pq = []
        time, result = 0, 0
        n = len(apples)
        
        while time < n or pq:
            if time < n and apples[time] > 0:
                heapq.heappush(pq, (time + days[time], apples[time]))
            
            while pq and pq[0][0] <= time:
                heapq.heappop(pq)
            
            if pq:
                result += 1
                pq[0] = (pq[0][0], pq[0][1] - 1)
                if pq[0][1] == 0:
                    heapq.heappop(pq)
            
            time += 1
        
        return result