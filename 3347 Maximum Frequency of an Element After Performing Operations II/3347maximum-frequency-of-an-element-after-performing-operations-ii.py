from sortedcontainers import SortedDict
class Solution:
    def maxFrequency(self, nums: List[int], num: int, numOperations: int) -> int:
        up = [n + num for n in nums]  # upper limit for each number
        down = [n - num for n in nums]  # lower limit for each number
        dictionary = SortedDict()

        # Add interval start and ends
        for d in down:
            dictionary[d] = dictionary.get(d, 0) + 1

        for u in up:
            # 0.1 is added so that two intervals starting and ending
            # at the same number count as an overlap of 2 instead of just 1.
            dictionary[u+0.1] = dictionary.get(u+0.1, 0) - 1

        # Add the actual numbers and their frequencies, encoded with +0.01
        for n in nums:
            dictionary[n+0.01] = dictionary.get(n+0.01, 0) + 1

        # Line sweep, searching for the maximum
        overlapping_intervals = 0
        answer = 0
        for num, val in dictionary.items():
            if abs(num - floor(num) - 0.01) < 0.01:  # num is an actual number in nums (ends in 0.01)
                possible_nums = overlapping_intervals - val  # Number of nums that can be extended to this num
                
                # Only consider the current frequency of the current number (val)
                # Plus as many extended numbers as numOperations allows
                answer = max(answer, val + min(possible_nums, numOperations))

            else:  # num is an extended version of a number in nums (ends in .0 or .1)
                overlapping_intervals += val  # Part of line sweep, add or subtract current interval
                answer = max(answer, min(overlapping_intervals, numOperations))  # Only consider as many overlapping intervals as numOperations allows

        return answer