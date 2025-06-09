class Solution:
    def maxGoodNumber(self, nums: List[int]) -> int:
      max_decimal_value=0
      for order in permutations(nums):
        binary_string=''.join(format(num,'b') for num in order)
        decimal_value=int(binary_string,2)
        max_decimal_value=max(max_decimal_value,decimal_value)  
      return max_decimal_value     