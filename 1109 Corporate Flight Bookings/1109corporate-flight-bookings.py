class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0] * n

        for first, last, seats in bookings:
            res[first - 1] += seats
            if last < n:
                res[last] -= seats

        # Prefix sum to get actual seat counts
        for i in range(1, n):
            res[i] += res[i - 1]

        return res


        # d = {}

        # for i, j, k in bookings:
        #     for a in range(i, j+1):
        #         if a not in d:
        #             d[a] = k
        #         else:
        #             d[a] += k
        # nd= dict(sorted(d.items()))

        # for i in range(1, n+1):
        #     if i not in nd:
        #         nd[i] = 0
        # print(nd)
        # nd= dict(sorted(nd.items()))
        # print(nd)
        # lst = []
        
        # for l in nd.values():
        #     lst.append(l)
        # return lst
        