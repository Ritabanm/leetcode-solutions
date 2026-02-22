class Solution:
    def sumDigitDifferences(self, nums: List[int]) -> int:

        m, n = len(nums), len(str(nums[0]))

        # determine the transpose of the strings of nums
        numStrs = zip(*[str(num) for num in nums])

        # determine the digit differences for each s
        cnts = list(chain(*[Counter(s).values() for s in numStrs]))

        # compute the answer
        return (m*m*n - sum(c*c for c in cnts) )//2