class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:

                # initiate a SortedList and find median.
        sl = SortedList(nums[:k])
        mdx = (k - 1) // 2 
        med = sl[mdx]

                # Determine number of operations required for sl.
        ans = opCnts = sum(abs(med - num) for num in nums[:k])

                # Iterate a sliding window
        for left, rght in zip(nums, nums[k:]):
                # adjust sl when window slides 
            sl.add(rght)
            sl.remove(left)

                # determine the previous and current median and opCnts
            prev, med = med, sl[mdx]
            opCnts+= abs(prev - rght) - abs(prev - left)

                # adjust the opCnts for the current median
            if k % 2 == 1:    opCnts -= abs(med - prev)
            elif prev <= med: opCnts -= (med - prev) * 2
            
                # update answer
            ans = min(ans, opCnts)

        return ans