class Solution:
    def recoverArray(self, nums):
        self.n, self.nums = len(nums) // 2, sorted(nums)

        small = self.nums[0]
        for x in self.nums[1:]:
            k = x - small # this represents 2 * k from the problem statement
            if k % 2 or not k: continue
            temp = self.valid(k)
            if temp: return temp
        return []

    def valid(self, k):
        counts = defaultdict(list)
        for i in range(len(self.nums) - 1, -1, -1):
            counts[self.nums[i]].append(i)

        # go through each value from smallest to largest
        # at each value check for corresponding (val + k)
        # keep track of which values are used when checking
        # ahead for the (val + k)
        # finally add (val + k / 2) if we find the corresponding
		# (val + k) as it is the value from the original array
        ans, used = [], [False] * len(self.nums)
        for i, v in enumerate(self.nums):
            if used[i]: continue
            if not counts[v + k]: return []
            used[counts[v + k].pop()] = True
            ans.append(v + k // 2)
        return ans