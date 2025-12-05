class Solution:
    def minDistinctFreqPair(self, nums: list[int]) -> list[int]:
        d, rgt = defaultdict(int), inf
        for num in nums:
            d[num]+=1
        (lft, lftCnt), keys = min(d.items()), sorted(d)
        for num, numCnt in d.items():
            if numCnt!=lftCnt and num<rgt:
                rgt = num
        return [-1,-1] if rgt == inf else [lft, rgt]