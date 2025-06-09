class Solution:
    def maxSumMinProduct(self, nums):
        max_val, stack, mod = 0, [], 10**9+7

        nums.append(0)

        for i,j in enumerate(nums):
            total = 0 
            while stack and stack[-1][0] >= j:
                x,y = stack.pop()
                total += y 
                max_val = max(max_val,total*x)
            stack.append((j,j+total))

        return max_val%mod