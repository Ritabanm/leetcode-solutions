class Solution:
    def minOperations(self, nums: List[int], target: int) -> int:

        sm, ans = sum(nums), 0                # <-- 1.
        if sm < target: return -1             #

        nums = list(map(lambda x: -x, nums))  #
        heapify(nums)                         #
                                              # <-- 2.
        while target:                         #
            num = -heappop(nums)              #
            sm-= num                          #
            
            if sm < target < num:             #
                                              # 
                ans+= 1                       #
                sm+= num                      # <-- 3.
                                              #
                heappush(nums, -num//2)       #
                heappush(nums, -num//2)       #

            target-= num * (num <= target)

        return ans                            # <-- 4.