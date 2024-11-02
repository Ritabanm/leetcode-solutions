class Solution:
    def divisibleTripletCount(self, nums: List[int], d: int) -> int:
        duplet_sums = collections.defaultdict(list)
        ans = 0

        for i, j in itertools.combinations(range(len(nums)), 2):
            duplet_sums[(nums[i] + nums[j]) % d].append((i, j))

        for k, val in enumerate(nums):
            # x + y MOD d == 0 is congruent to (x MOD d + y MOD d) MOD d == 0
            # One solution is (x MOD d + y MOD d) == d
            target_key = (d - val % d) % d
            ans += sum(1 for (i, j) in duplet_sums[target_key] if j < k)

        return ans