from typing import List
from functools import lru_cache

class Solution:
    def minMaxWaitingTime(self, demand: List[int], fuel: List[int]) -> int:
        n = len(demand)
        
        # State: (car_index, f0, f1, t0, t1)
        # f0, f1: remaining fuel in dispenser 0 and 1
        # t0, t1: remaining busy time for dispenser 0 and 1
        @lru_cache(None)
        def dp(i: int, f0: int, f1: int, t0: int, t1: int):
            if i == n:
                return (0, 0)  # (cars_served, max_wait)
            
            best_cars = -1
            best_max_wait = float('inf')
            
            # Try assigning car i to Dispenser 0
            if f0 >= demand[i]:
                wait = t0
                nt0 = demand[i]
                nt1 = max(0, t1 - wait)
                nf0 = f0 - demand[i]
                
                cars, max_w = dp(i + 1, nf0, f1, nt0, nt1)
                total_cars = 1 + cars
                total_max_wait = max(wait, max_w)
                
                if total_cars > best_cars or (total_cars == best_cars and total_max_wait < best_max_wait):
                    best_cars = total_cars
                    best_max_wait = total_max_wait
            
            # Try assigning car i to Dispenser 1
            if f1 >= demand[i]:
                wait = t1
                nt1 = demand[i]
                nt0 = max(0, t0 - wait)
                nf1 = f1 - demand[i]
                
                cars, max_w = dp(i + 1, f0, nf1, nt0, nt1)
                total_cars = 1 + cars
                total_max_wait = max(wait, max_w)
                
                if total_cars > best_cars or (total_cars == best_cars and total_max_wait < best_max_wait):
                    best_cars = total_cars
                    best_max_wait = total_max_wait
            
            # If neither dispenser can serve the car, process terminates
            if best_cars == -1:
                return (0, 0)
                
            return (best_cars, best_max_wait)

        # To find the absolute maximum cars possible first, we can run a helper or structure 
        # the DP to prioritize maximum cars, then minimal max wait.
        # Let's write a wrapper to find the max possible cars across all paths:
        
        memo = {}
        def solve(i, f0, f1, t0, t1):
            if i == n:
                return (0, 0)
            state = (i, f0, f1, t0, t1)
            if state in memo:
                return memo[state]
            
            res = (-1, float('inf'))
            
            # Option 0
            if f0 >= demand[i]:
                wait = t0
                nt0 = demand[i]
                nt1 = max(0, t1 - wait)
                nf0 = f0 - demand[i]
                c, w = solve(i + 1, nf0, f1, nt0, nt1)
                res = max(res, (1 + c, max(wait, w)), key=lambda x: (x[0], -x[1]))
                
            # Option 1
            if f1 >= demand[i]:
                wait = t1
                nt1 = demand[i]
                nt0 = max(0, t0 - wait)
                nf1 = f1 - demand[i]
                c, w = solve(i + 1, f0, nf1, nt0, nt1)
                res = max(res, (1 + c, max(wait, w)), key=lambda x: (x[0], -x[1]))
                
            if res[0] == -1:
                res = (0, 0)
                
            memo[state] = res
            return res

        total_cars, max_wait = solve(0, fuel[0], fuel[1], 0, 0)
        
        # If no cars could be served based on problem description
        if total_cars == 0 and (fuel[0] < demand[0] and fuel[1] < demand[0]):
            return -1
            
        # We need to return the minimum possible value of the maximum waiting time 
        # among all assignments that maximize the number of served cars.
        # Our key function `max(..., key=lambda x: (x[0], -x[1]))` naturally maximizes cars 
        # and minimizes max_wait.
        
        # Check if even car 0 failed
        if fuel[0] < demand[0] and fuel[1] < demand[0]:
            return -1
            
        return max_wait