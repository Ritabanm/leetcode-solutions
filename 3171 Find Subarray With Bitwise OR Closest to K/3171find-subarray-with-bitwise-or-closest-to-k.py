from typing import List

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        """
        For every contiguous subarray compute its OR (in compressed form via `cur`),
        and return the minimum absolute difference between any such OR and k.
        """

        res = set()   # all distinct OR values of all subarrays (optional, can be avoided)
        cur = set()   # distinct OR values of subarrays ending at previous index

        for x in nums:
            # Extend every previous-ending subarray by x, and include [x] itself.
            # cur becomes the set of distinct ORs for subarrays ending at current index.
            cur = {x | y for y in cur} | {x}

            # Add these into the global set of OR-values
            res |= cur

        # Now res contains distinct ORs for every non-empty subarray.
        # Return the minimal absolute difference to k.
        return min(abs(val - k) for val in res)