class Solution:
    def minimumTime(self, nums1: List[int], nums2: List[int], x: int) -> int:
        total_initial = sum(nums1)
        total_rate = sum(nums2)
        n = len(nums1)
        counters = sorted(zip(nums2, nums1))  # (rate, initial); sorted in increasing order of rate
        
        # Require that counters_end_idx >= t
        @lru_cache(None)
        def calc_max_reduction(counters_end_idx: int, t: int) -> int:
            if t == 0:
                return 0
            
            # Get the last counter (with highest rate)
            rate, initial = counters[counters_end_idx - 1]

            # This is the case where we reduce this counter at time t
            res = calc_max_reduction(counters_end_idx - 1, t - 1) + rate * t + initial
            
            # This is the case where we don't reduce this counter at time t
            # (Not available if items_end == n_steps since we would be forced to reduce the counter)
            if counters_end_idx > t:
                res = max(res, calc_max_reduction(counters_end_idx - 1, t))

            return res

        for t in range(0, n + 1):
            max_reduction = calc_max_reduction(n, t)
            if total_initial + t * total_rate - max_reduction <= x:
                return t

        return -1