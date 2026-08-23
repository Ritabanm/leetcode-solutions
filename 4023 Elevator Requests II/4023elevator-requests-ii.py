class Solution:
    def elevatorRequests(self, n: int, start: int, requests: list[int]) -> int:

        # Requests below and above the starting floor.
        # Store only their distances from 'start', sorted from nearest to farthest.
        left = sorted(start - x for x in requests if x < start)
        right = sorted(x - start for x in requests if x > start)

        L = len(left)
        R = len(right)
        total = L + R

        # memo[left_done][right_done][side]
        #
        # side:
        #   0 -> still at the starting floor
        #   1 -> currently at the last served left request
        #   2 -> currently at the last served right request
        #
        # Stores the minimum future waiting cost from this state.
        memo = [[[-1] * 3 for _ in range(R + 1)] for _ in range(L + 1)]

        def dp(left_done, right_done, side):

            # Everyone has been served.
            if left_done == L and right_done == R:
                return 0

            if memo[left_done][right_done][side] != -1:
                return memo[left_done][right_done][side]

            # Figure out which floor we're currently standing on.
            if side == 0:
                current_floor = start
            elif side == 1:
                current_floor = start - left[left_done - 1]
            else:
                current_floor = start + right[right_done - 1]

            # How many people are still waiting?
            remaining = total - left_done - right_done

            answer = float("inf")

            # Option 1:
            # Serve the next closest unfinished request on the left.
            if left_done < L:

                next_floor = start - left[left_done]
                distance = abs(current_floor - next_floor)

                cost = distance * remaining
                answer = min(
                    answer,
                    cost + dp(left_done + 1, right_done, 1)
                )

            # Option 2:
            # Serve the next closest unfinished request on the right.
            if right_done < R:

                next_floor = start + right[right_done]
                distance = abs(current_floor - next_floor)

                cost = distance * remaining
                answer = min(
                    answer,
                    cost + dp(left_done, right_done + 1, 2)
                )

            memo[left_done][right_done][side] = answer
            return answer

        return dp(0, 0, 0)