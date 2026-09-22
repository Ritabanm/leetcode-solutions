class Solution(object):
    def largestPower(self, nums):
        groups = [list(range(len(nums)))]
        ans = []

        for b in range(14, -1, -1):
            s = 0

            for k, group in enumerate(groups):
                ones = [i for i in group if (nums[i] >> b) & 1]

                if len(ones) == len(group):
                    s += len(group)
                else:
                    zeros = [i for i in group if not ((nums[i] >> b) & 1)]
                    groups[k:k + 1] = [ones, zeros]
                    ans.append(s + len(ones))
                    break
            else:
                ans.append(len(nums))

        return ans