class Solution:
    def equalizeWater(self, buckets: List[int], loss: int) -> float:

        def is_feasible(target):
            surplus = 0 
            deficit = 0 
            for water_level in buckets:
                if water_level > target:
                    surplus += water_level - target
                elif water_level < target:
                    deficit += target - water_level
            return surplus*(1-loss/100.0)>=deficit

        start = min(buckets)
        end = max(buckets)

        while end-start>10**-6:
            mid = (start+end)/2
            if is_feasible(mid):
                # Check for bigger value
                start = mid
            else:
                # Shrink the rank
                end = mid

        return start 
        