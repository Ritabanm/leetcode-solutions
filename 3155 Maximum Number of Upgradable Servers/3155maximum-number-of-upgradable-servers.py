from math import ceil
class Solution:
    def maxUpgrades(self, count: List[int], upgrade: List[int], sell: List[int], money: List[int]) -> List[int]:
        return [count[i] - ceil(max(count[i]*upgrade[i]-money[i], 0)/(sell[i]+upgrade[i])) for i in range(len(count))]