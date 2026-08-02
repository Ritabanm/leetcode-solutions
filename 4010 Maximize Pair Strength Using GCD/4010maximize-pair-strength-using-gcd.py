from math import gcd

class Solution:
    def maxPairStrength(self, nums: list[int]) -> int:
        max_strength = 0
        n = len(nums)
        
        for i in range(n):
            for j in range(i + 1, n):
                g = gcd(nums[i], nums[j])
                strength = (nums[i] * nums[j]) // (g * g)
                
                if strength > max_strength:
                    max_strength = strength
                    
        return max_strength