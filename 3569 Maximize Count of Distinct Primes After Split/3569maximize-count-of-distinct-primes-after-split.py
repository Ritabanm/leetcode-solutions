class SegmentTree:
    def __init__(self, nums):
        self.n = len(nums)
        self.p = 1
        
        while self.p < self.n:
            self.p <<= 1

        self.sm = [0] * (2 * self.p)
        self.prefMax = [0] * (2 * self.p)
        
        for i, v in enumerate(nums):
            self.sm[self.p + i] = v
            self.prefMax[self.p + i] = v
            
        for i in range(self.p - 1, 0, -1):
            left, right = 2 * i, 2 * i + 1
            self.sm[i] = self.sm[left] + self.sm[right]
            self.prefMax[i] = max(self.prefMax[left], self.sm[left] + self.prefMax[right])
        

    def update(self, idx, delta):
        cur = idx + self.p
        self.sm[cur] += delta
        self.prefMax[cur] += delta

        cur //= 2

        while cur > 0:
            left, right = 2 * cur, 2 * cur + 1
            self.sm[cur] = self.sm[left] + self.sm[right]
            self.prefMax[cur] = max(self.prefMax[left], self.sm[left] + self.prefMax[right])
            cur //= 2

    def getMaxPref(self):
        return self.prefMax[1]

class Solution:
    def maximumCount(self, nums: List[int], queries: List[List[int]]) -> List[int]:
       
        n = len(nums)

        def sieve(n):
            P = [True] * (n + 1)
            
            P[0] = False
            P[1] = False
            
            for i in range(2, int(sqrt(n)) + 1):
                if P[i]:
                    for j in range(i * i, n + 1, i):
                        P[j] = False
                        
            return P

        isPrime = sieve(max(nums + [v for _, v in queries]))

        def removePrime(p, idx):
            nonlocal unq, seg
            
            mp = D[p]
            s = mp["set"]
            oldCnt = len(s)

            if oldCnt >= 2:
                while mp["minheap"] and mp["minheap"][0] not in mp["set"]:
                    heapq.heappop(mp["minheap"])
                oldFirst = mp["minheap"][0]

                while mp["maxheap"] and -mp["maxheap"][0] not in mp["set"]:
                    heapq.heappop(mp["maxheap"])
                oldLast = -mp["maxheap"][0]

            s.remove(idx)

            if oldCnt == 1:
                unq -= 1
                del D[p]

            elif oldCnt == 2:

                for pos in (oldFirst, oldLast):
                    old = arr[pos]
                    seg.update(pos, -old)
                    arr[pos] = 0

            elif oldCnt > 2:
                if idx == oldFirst:
                    while mp["minheap"] and mp["minheap"][0] not in s:
                        heapq.heappop(mp["minheap"])

                    newFirst = mp["minheap"][0]

                    seg.update(idx, -1)
                    arr[idx] = 0

                    seg.update(newFirst, 1)
                    arr[newFirst] = 1

                elif idx == oldLast:
                    while mp["maxheap"] and -mp["maxheap"][0] not in s:
                        heapq.heappop(mp["maxheap"])
                    
                    newLast = -mp["maxheap"][0]

                    seg.update(idx, 1)
                    arr[idx] = 0

                    seg.update(newLast, -1)
                    arr[newLast] = -1

        def insertPrime(p, idx):
            nonlocal unq, seg

            mp = D.get(p)

            if mp is None:
                mp = {"set": set(), "minheap": [], "maxheap": []}
                D[p] = mp
                oldCnt = 0
            
            else:
                oldCnt = len(mp["set"])

                # update min and max heaps by removing no longer present values
                if oldCnt >= 2:
                    while mp["minheap"] and mp["minheap"][0] not in mp["set"]:
                        heapq.heappop(mp["minheap"])
                    oldFirst = mp["minheap"][0]

                    while mp["maxheap"] and -mp["maxheap"][0] not in mp["set"]:
                        heapq.heappop(mp["maxheap"])
                    oldLast = -mp["maxheap"][0]

            mp["set"].add(idx)
            heapq.heappush(mp["minheap"], idx)
            heapq.heappush(mp["maxheap"], -idx)

            if oldCnt == 0:
                unq += 1
            
            elif oldCnt == 1:
                other = next(x for x in mp["set"] if x != idx)

                newFirst, newLast = (min(idx, other), max(idx, other))

                prevVal = arr[newFirst]
                seg.update(newFirst, 1 - prevVal)
                arr[newFirst] = 1

                prevVal = arr[newLast]
                seg.update(newLast, -1 - prevVal)
                arr[newLast] = -1

            elif oldCnt >= 2:

                if idx < oldFirst:

                    # new first
                    prevVal = arr[idx]
                    seg.update(idx, 1 - prevVal)
                    arr[idx] = 1

                    # update old first to 0
                    seg.update(oldFirst, -1)
                    arr[oldFirst] = 0

                elif idx > oldLast:
                    # new last
                    prevVal = arr[idx]
                    seg.update(idx, -1 - prevVal)
                    arr[idx] = -1

                    # update old last to 0
                    seg.update(oldLast, 1)
                    arr[oldLast] = 0



        D = {}
        unq = 0
        arr = [0] * n

        seg = SegmentTree(arr)

        for i, v in enumerate(nums):
            if isPrime[v]:
                insertPrime(v, i)

        res = []

        for idx, val in queries:
            old = nums[idx]

            if val == old:
                res.append(unq + seg.getMaxPref())
                continue

            if isPrime[old]:
                removePrime(old, idx)
            
            if isPrime[val]:
                insertPrime(val, idx)

            nums[idx] = val

            res.append(unq + seg.getMaxPref())
        
        return res
        