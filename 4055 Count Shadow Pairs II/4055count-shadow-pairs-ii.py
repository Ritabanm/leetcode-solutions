class Solution:
    def shadowPairs(self, nums: List[int]) -> int:
        # tie order: ask, then open, then close
        # keeps low < high strict, high <= ceiling inclusive
        ASK, OPEN, CLOSE = 0, 1, 2

        def count_crossing(left, right):
            events = []

            seen = SortedList([inf])  # left walks paused at the cut
            for low in reversed(left):
                ceiling = seen[seen.bisect_right(low)]  # window (low, ceiling]
                events += [(low, OPEN, low), (ceiling, CLOSE, low)]
                seen.add(low)

            seen = SortedList([-inf])  # right walks paused at the cut
            for high in right:
                floor = seen[seen.bisect_left(high) - 1]
                events.append((high, ASK, floor))
                seen.add(high)

            count, active = 0, SortedList()  # lows of open windows
            for value, kind, payload in sorted(events): # payload: low, or floor for ASK
                if kind == OPEN:
                    active.add(payload)
                elif kind == CLOSE:
                    active.remove(payload)
                else:  # floor <= low < high <= ceiling
                    count += len(active) - active.bisect_left(payload)
            return count

        def solve(arr):
            if len(arr) <= 1:
                return 0
            mid = len(arr) // 2
            left, right = arr[:mid], arr[mid:]
            return solve(left) + solve(right) + count_crossing(left, right)

        return solve(nums)