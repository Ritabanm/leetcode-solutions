class Solution:
    def isPossible(self, n, k, budget, composition, stock, costs, fixed_alloy):
        for i in range(k):
            calBudget = 0
            for j in range(n):
                required = composition[i][j] * fixed_alloy
                required -= stock[j]
                if required > 0:
                    calBudget += required * costs[j]
            if calBudget <= budget:
                return True
        return False
    
    def maxNumberOfAlloys(self, n, k, budget, composition, stock, cost):
        low = 1
        high = 1e9
        ans = 0
        while low <= high:
            mid = low + (high - low) // 2
            if self.isPossible(n, k, budget, composition, stock, cost, mid):
                low = mid + 1
                ans = mid
            else:
                high = mid - 1
        return int(ans)