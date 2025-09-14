class Solution:
    def countEvenlyGoodIntegers(self, l: int, r: int) -> int:
        
        def count_up_to(n: str) -> int:
            memo = {}
            
            def dp(index: int, even_count: int, is_less: bool, is_started: bool) -> int:
                if index == len(n):
                    # If the number has started (not all leading zeros), check if even_count is even
                    return 1 if is_started and (even_count % 2 == 0) else 0
                
                state = (index, even_count, is_less, is_started)
                if state in memo:
                    return memo[state]
                
                limit = int(n[index]) if not is_less else 9
                res = 0
                
                for digit in range(limit + 1):
                    next_is_less = is_less or (digit < limit)
                    
                    if not is_started and digit == 0:
                        # Continuing leading zeros
                        res += dp(index + 1, even_count, next_is_less, False)
                    else:
                        # Number has started, check if current digit is even (0, 2, 4, 6, 8)
                        is_digit_even = 1 if (digit % 2 == 0) else 0
                        res += dp(index + 1, even_count + is_digit_even, next_is_less, True)
                
                memo[state] = res
                return res

            return dp(0, 0, False, False)

        return count_up_to(str(r)) - count_up_to(str(l - 1))