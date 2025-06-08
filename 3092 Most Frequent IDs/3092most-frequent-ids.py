class Solution:
    def mostFrequentIDs(self, nums: List[int], freq: List[int]) -> List[int]:
        res = []
        maxf = []
        tbl = defaultdict(int)
        for n, f in zip(nums, freq):
            tbl[n] += f
            if tbl[n] <= 0: del tbl[n]
            heapq.heappush(maxf, (-tbl.get(n, 0), n))
            while maxf and tbl.get(maxf[0][1], 0) != -maxf[0][0]: heapq.heappop(maxf)
            res.append(-maxf[0][0] if maxf else 0)
        return res