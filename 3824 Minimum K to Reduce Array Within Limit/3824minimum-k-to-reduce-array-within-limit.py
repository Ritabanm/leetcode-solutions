class Solution:
    def minimumK(self, nums: List[int]) -> int:

        n = currK = sum(nums)

        for k in range(n):
            if currK > k**3: continue
            currK = k
            break
           
        while True:
            ops = sum(map(lambda x: ceil(x/currK), nums))
            if ops <= currK * currK:
                return currK
            currK+= 1
    