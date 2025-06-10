class Solution:
    def maximumBeauty(self, flowers: List[int]) -> int:
        flower_type2min_prefix = {}
        greedy_carry = 0  # only carry positive flowers
        ans = -inf
        for flower in flowers:
            if flower in flower_type2min_prefix:
                # need manual adjustment for first and last flower (especially for negative ones)
                ans = max(ans, greedy_carry - flower_type2min_prefix[flower] + flower + (flower if flower < 0 else 0))
                flower_type2min_prefix[flower] = min(flower_type2min_prefix[flower], greedy_carry)
            else:
                flower_type2min_prefix[flower] = greedy_carry
            if flower > 0:
                greedy_carry += flower
        return ans