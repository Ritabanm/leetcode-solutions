import heapq
from collections import deque

class Solution:
    def primeSubarray(self, nums: list[int], k: int) -> int:
        n = len(nums)
        maxNum = max(nums, default=0)
        isPrime = [True] * (maxNum + 1)
        if maxNum >= 0:
            isPrime[0] = False
        if maxNum >= 1:
            isPrime[1] = False
        for p in range(2, int(maxNum**0.5) + 1):
            if not isPrime[p]:
                continue
            for multiple in range(p*p, maxNum+1, p):
                isPrime[multiple] = False

        minHeap = []
        maxHeap = []
        primeDeque = deque()
        cnt = 0
        leftBound = -1

        for idx, num in enumerate(nums):
            if num > maxNum or not isPrime[num]:
                if len(primeDeque) > 1:
                    cnt += primeDeque[-2] - leftBound
                continue

            heapq.heappush(minHeap, (num, idx))
            heapq.heappush(maxHeap, (-num, idx))
            primeDeque.append(idx)

            while primeDeque and (-maxHeap[0][0] - minHeap[0][0]) > k:
                leftBound = primeDeque.popleft()
                while minHeap and minHeap[0][1] <= leftBound:
                    heapq.heappop(minHeap)
                while maxHeap and maxHeap[0][1] <= leftBound:
                    heapq.heappop(maxHeap)

            if len(primeDeque) > 1 and (-maxHeap[0][0] - minHeap[0][0]) <= k:
                cnt += primeDeque[-2] - leftBound

        return cnt