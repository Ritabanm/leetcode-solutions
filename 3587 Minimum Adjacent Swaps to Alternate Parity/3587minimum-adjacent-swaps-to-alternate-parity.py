class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        def countSwaps(start):
            return sum(map(abs,map(sub, ones,range(start,n,2))))
     

        ones = [i for i, num in enumerate(nums) if num%2 == 1]
        n, m = len(nums), 2 * len(ones)
       
        if m == n:                                          # 1)
            return min(countSwaps(0), countSwaps(1))

        if m == n + 1:                                      # 2)
            return countSwaps(0)

        if m == n - 1:                                      # 3)
            return countSwaps(1)

        return -1                                           # 4)