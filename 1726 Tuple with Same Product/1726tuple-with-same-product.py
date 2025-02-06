from collections import defaultdict
class Solution:
    def tupleSameProduct(self, nums):
        product_map = defaultdict(list)
        n = len(nums)
        for i in range(n):
            for j in range(i+1, n):
                product = nums[i]*nums[j]
                product_map[product].append((nums[i], nums[j]))
        result = 0
        for product, pairs in product_map.items():
            k = len(pairs)
            if k>1:
                combinations = (k*(k-1))//2
                result+=combinations*8
        return result