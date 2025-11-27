class Solution:
    def minimumTime(self, power):
        n = len(power)

        @lru_cache(None)
        def function(bitmask,gain):
            if bitmask == (1<<n) - 1:
                return 0

            min_val = float("inf")

            for i in range(n):
                if not (1<<i)&bitmask:
                    min_val = min(min_val,math.ceil(power[i]/gain) + function(bitmask|(1<<i),gain+1))

            return min_val

        return function(0,1)




        