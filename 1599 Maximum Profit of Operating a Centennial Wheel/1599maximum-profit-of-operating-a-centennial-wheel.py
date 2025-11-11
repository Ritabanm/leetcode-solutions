class Solution:
    def minOperationsMaxProfit(self, customers: List[int], boardingCost: int, runningCost: int) -> int:
        max_profit = 0
        current_profit = 0
        max_rotation = -1
        waiting_customers = 0
        total_boarded = 0
        rotations = 0
        
        while waiting_customers > 0 or rotations < len(customers):
            if rotations < len(customers):
                waiting_customers += customers[rotations]
            board = min(4, waiting_customers)
            total_boarded += board
            waiting_customers -= board
            current_profit = total_boarded * boardingCost - (rotations + 1) * runningCost
            if current_profit > max_profit:
                max_profit = current_profit
                max_rotation = rotations + 1
            rotations += 1
            
        return max_rotation if max_profit > 0 else -1