class Solution:
    def sumDivisibleByK(self, nums: List[int], k: int) -> int:

        ctr = Counter(nums)
        return sum(num * ctr[num] for num in ctr if ctr[num] % k == 0)