class Solution:
    def countPairs(self, nums: List[int]) -> int:

        d, ans = defaultdict(list), 0

        mx = int(log10(max(nums)))+1                            # <- 1
        nums = map(lambda x: (str(x).rjust(mx, '0')), nums)     # <- 2

        for num in nums:                                        # <- 3
            d[''.join(sorted(num))]. append(num)              

        for key in d:
            for str1, str2 in combinations(d[key],2):           # <- 4
             if sum(c1 != c2 for c1, c2 in zip(str1, str2)) < 3:
                ans+= 1

        return ans                                              # <- 5