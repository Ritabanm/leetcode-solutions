class Solution:
    def maxSpending(self, values: List[List[int]]) -> int:
        n, m = len(values), len(values[0])
        ans = 0
        indexes = [m-1]*n
        for i in range(n*m):
            min_value, min_index = min((values[k][indexes[k]],k) for k in range(n) if indexes[k]>=0)

            ans+=(i+1)*min_value
            indexes[min_index]-=1
        return ans