mx = lambda x, y: x if x > y else y

class Solution:
    def maximumSum(self, nums: List[int]) -> int:

        heaps = [[0] * 3 for _ in range(3)]
        for num in nums:
            heappushpop(heaps[num % 3], num)

        triplet = [max(x) for x in heaps]

        if 0 in triplet: ans = 0
        else: ans = sum(triplet)    

        for heap in heaps:
            if heap[0] == 0: continue
            ans = mx(ans, sum(heap))

        return ans