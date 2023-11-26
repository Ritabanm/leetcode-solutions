class Solution:
    def halveArray(self, nums: List[int]) -> int:
        heap = []
        for num in nums:
            heappush(heap,-1 * num)

        initalSum = sum(nums)
        targetSum = initalSum / 2
        k = 0

        while  initalSum > targetSum:
            val = heappop(heap)
            heappush(heap,val / 2)
            initalSum -= (-1 * (val / 2))
            k = k + 1
            
        return k