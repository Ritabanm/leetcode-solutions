class Solution:
    def maxIntersectionCount(self, A: List[int]) -> int:
        '''
        a zig or a zag (a line up or down) increases the number of intersections

        no two consec y_i's have the same y coord

        original thought was line sweep

        also could be fenwick using standardized points

        what we are trying to do is essentially draw each line for sweep line
        '''
        N = len(A)

        if N <= 2:
            return 1

        for i in range(N):
            A[i] *= 2

        events = []

        mn = min(A[0], A[1])
        mx = max(A[0], A[1])
        events.append((mn, 1))
        events.append((mx, -1))

        for y1, y2 in zip(A[1:], A[2:]):
            mn = min(y1, y2)
            mx = max(y1, y2)

            if y1 < y2:
                events.append((mn + 1, 1))
                events.append((mx, -1))

            else:
                events.append((mn, 1))
                events.append((mx - 1, -1))


        events.sort(key=lambda x: (x[0], -x[1]))

        best = 0
        total = 0

        # print(events)

        for t in events:
            total += t[1]
            best = max(best, total)

        return best



        

        