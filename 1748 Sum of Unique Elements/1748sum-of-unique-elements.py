class Solution:
    def sumOfUnique(self, nums):
        countz = Counter(nums)
        res = []

        for item, count in countz.items():
            if count==1:
                res.append(item)
        return sum(res)