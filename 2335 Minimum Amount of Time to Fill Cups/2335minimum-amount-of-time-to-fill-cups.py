class Solution:
    def fillCups(self, amount: List[int]) -> int:
        heap = []
        for i in amount:
            if i != 0:
                heapq.heappush(heap, -i)
        
        resp = 0
        while heap:
            print(heap)
            if len(heap) >= 2:
                x1 = -heapq.heappop(heap)
                x2 = -heapq.heappop(heap)
                x1 -= 1
                x2 -= 1
                if x1 != 0:
                    heapq.heappush(heap, -x1)
                if x2 != 0:
                    heapq.heappush(heap, -x2)
                resp += 1
            else:
                x1 = -heapq.heappop(heap)
                resp += x1
        return resp
        