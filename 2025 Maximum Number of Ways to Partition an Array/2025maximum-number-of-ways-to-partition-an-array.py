class Solution:
    def waysToPartition(self, nums: List[int], k: int) -> int:
        before = {k:0}; after = {}; counter = Counter(nums)
        p = list(accumulate(nums))
        n = len(nums)
        for i, num in enumerate(nums[:n-1]):
            before[num] = max(before.get(num, 0), after.get(num, 0))
            counter[nums[i]] -= 1
            if counter[nums[i]] == 0: del counter[nums[i]]
            
            diff = 2 * p[i] - p[-1]
            if (k + diff) in before: before[k + diff] += 1
            if (k - diff) in counter: after[k - diff] = after.get(k - diff, 0) + 1
        return max(max([0] + list(before.values())), max([0] + list(after.values())))