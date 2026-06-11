class Solution:
    def maximumSaleItems(self, items: List[List[int]], budget: int) -> int:

        mn = inf
        arr = [0] * len(items)
        cn = defaultdict(int)
        factors = defaultdict(int)

        mx = 0
        for i in range(len(items)):
            cn[items[i][0]] += 1
            mx = max(mx, items[i][0])
            mn = min(mn, items[i][1])
        
        for i in range(len(items)):
            f = items[i][0]
            cnt = 1
            if items[i][1] >= mn * 2: continue
            if f not in factors:
                while f * cnt <= mx:
                    arr[i] += cn[f * cnt]
                    cnt += 1
                arr[i] -= 1

                factors[f] = arr[i]
            else:
                arr[i] = factors[f]

        # print(arr)

        # print(mn)

        heap = []

        for i in range(len(items)):
            if arr[i] != 0:
                heapq.heappush(heap, (items[i][1], i))
        
        # print(heap)

        sm = 0
        while heap:
            pr, i = heapq.heappop(heap)

            q = min(arr[i], budget // pr)
            budget -= (q * pr)
            sm += (q * 2)
        
        return (sm + budget // mn)


