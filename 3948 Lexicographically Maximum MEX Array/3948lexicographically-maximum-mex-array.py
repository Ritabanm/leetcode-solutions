from collections import Counter

class Solution:
    def maximumMEX(self, nums: List[int]) -> List[int]:

        freq = Counter(nums)

        mex = 0

        while freq[mex] > 0:
            mex += 1

        result = []

        i = 0
        n = len(nums)

        while i < n:

            current_mex = mex

            result.append(current_mex)

            if current_mex == 0:

                freq[nums[i]] -= 1

                if freq[nums[i]] == 0 and nums[i] < mex:
                    mex = nums[i]

                i += 1

                continue

            seen = set()

            need = current_mex

            while need > 0:

                value = nums[i]

                freq[value] -= 1

                if value < current_mex and value not in seen:
                    seen.add(value)
                    need -= 1

                if freq[value] == 0 and value < mex:
                    mex = value

                i += 1

            while freq[mex] > 0:
                mex += 1

        return result