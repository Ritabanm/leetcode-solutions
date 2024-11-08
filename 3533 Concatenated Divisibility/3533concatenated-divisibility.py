class Solution:
    def concatenatedDivisibility(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 10^len(num) mod k
        power = [pow(10, len(str(num)), k) for num in nums]
        # try smaller nums first
        idxs = sorted(range(n), key=lambda i: nums[i])
        # full mask = all nums used
        all_used = (1 << n) - 1

        @lru_cache(None)
        def solve(used: int, rem: int) -> Optional[List[int]]:
            if used == all_used:
                return [] if rem == 0 else None

            for i in idxs:
                if used & (1 << i):       # skip if already used
                    continue
                new_rem = (rem * power[i] + nums[i]) % k
                suffix = solve(used | (1 << i), new_rem)
                if suffix is not None:
                    # first successful branch is lex-min overall
                    return [nums[i]] + suffix

            return None

        result = solve(0, 0)
        return result or []