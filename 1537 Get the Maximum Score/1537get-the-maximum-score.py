class Solution:
    def maxSum(self, nums1: List[int], nums2: List[int]) -> int:
        it1 = iter(nums1)
        it2 = iter(nums2)
        sum1 = sum2 = 0
        try:
            while True:
                num1 = next(it1)
                sum1 += num1
                num2 = next(it2)
                sum2 += num2
                while num1 != num2:
                    if num1 > num2:
                        num2 = next(it2)
                        sum2 += num2
                    else:
                        num1 = next(it1)
                        sum1 += num1
                sum1 = sum2 = max(sum1, sum2)
        except StopIteration:
            sum1 += sum(it1)
            sum2 += sum(it2)
            return max(sum1, sum2) % 1_000_000_007