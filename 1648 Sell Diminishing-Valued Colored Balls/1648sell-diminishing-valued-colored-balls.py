class Solution:
    def maxProfit(self, inventory: List[int], orders: int) -> int:
        mod = 10**9 + 7
        inventory.append(0)
        inventory.sort()

        result = 0
        active = 1

        for i in range(len(inventory) - 1, 0, -1):
            if orders == 0:
                break
            cur = inventory[i]
            next = inventory[i - 1]

            if cur == next:
                active += 1
                continue

            if orders >= (cur - next) * active:
                profit = (cur + next + 1) * (cur - next) * active // 2
                result = (result + profit) % mod
                orders -= (cur - next) * active
            else:
                full_step = orders // active
                left = orders % active
                profit = (cur + cur - full_step + 1) * full_step * active // 2
                profit += left * (cur - full_step)
                result = (result + profit) % mod
                break

            active += 1


        return result % mod