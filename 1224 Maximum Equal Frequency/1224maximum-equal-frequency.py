class Solution:
    def maxEqualFreq(self, nums):
        dict1, dict2, max_len = collections.defaultdict(int), collections.defaultdict(int), 0

        for i,j in enumerate(nums):
            dict1[j] += 1
            dict2[dict1[j]] += 1

            val = dict2[dict1[j]]*dict1[j]

            if val == i+1 and i != len(nums)-1:
                max_len = max(max_len,i+2)
            elif val == i:
                max_len = max(max_len,i+1)

        return max_len




        