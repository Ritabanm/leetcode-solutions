class Solution:
    def unmarkedSumArray(self, nums: List[int], 
                               queries: List[List[int]]) -> List[int]:

        n, sm = len(nums), sum(nums)
        unmarked, ans = set(range(n)), []

        heap = list(zip(nums,range(len(nums))))
        heapify(heap)

        for idx, k in queries:

            if idx in unmarked:
                sm -= nums[idx]
                unmarked.discard(idx)

            while k and heap:

                num, idx = heappop(heap) 

                if idx in unmarked:               
                    unmarked.discard(idx)
                    k-= 1
                    sm-= num

            ans.append(sm)

        return ans