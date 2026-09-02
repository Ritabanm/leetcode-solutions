class Solution:

    def minOperations(self, nums: list[int], sum: int) -> int:

        def generateSequence(num):

            arr = []
            curr = num
            ops = 0

            # Repeatedly multiply by 2
            while curr <= sum:

                arr.append((curr, ops))

                ops += 1
                curr *= 2

            # Repeatedly divide by 2
            curr = num // 2
            ops = 1

            while curr != 0:

                arr.append((curr, ops))

                ops += 1
                curr //= 2

            return arr

        def solve(idx, target):

            # Target successfully formed
            if target == 0:
                return 0

            # No numbers left
            if idx == n:
                return float('inf')

            # Already calculated
            if dp[idx][target] != -1:
                return dp[idx][target]

            # Option 1: Skip current number
            best = solve(idx + 1, target)

            # Option 2: Choose one transformed value
            for val, steps in sequence[idx]:

                if target - val < 0:
                    continue

                best = min(
                    best,
                    steps + solve(idx + 1, target - val)
                )

            dp[idx][target] = best

            return best

        n = len(nums)

        # Generate possible values for every number
        sequence = []

        for i in nums:
            sequence.append(generateSequence(i))

        # dp[idx][target]
        dp = [[-1] * (sum + 1) for _ in range(n)]

        val = solve(0, sum)

        if val == float('inf'):
            return -1

        return val