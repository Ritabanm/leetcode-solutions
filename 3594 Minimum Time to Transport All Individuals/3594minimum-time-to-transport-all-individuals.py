class Solution:
    def minTime(self, n: int, k: int, m: int, time: List[int], mul: List[float]) -> float:
        heap = [(0.0, 0, 0, 0)]
        seen = dict()

        full_mask = (1 << n) - 1

        while heap:
            t, p, mask, j = heappop(heap)
            state = (p, mask, j)
            if state in seen and seen[state] <= t:
                continue
            seen[state] = t
            if mask == full_mask and p == 1:
                return round(t, 5)

            if p == 0:
                camp = [i for i in range(n) if not (mask >> i) & 1]
                for r in range(1, min(k, len(camp)) + 1):
                    for group in combinations(camp, r):
                        cross = max(time[i] for i in group) * mul[j]
                        new_j = (j + floor(cross)) % m
                        new_mask = mask
                        for i in group:
                            new_mask |= (1 << i)
                        heappush(heap, (t + cross, 1, new_mask, new_j))
            else:
                dst = [i for i in range(n) if (mask >> i) & 1]
                for i in dst:
                    return_time = time[i] * mul[j]
                    new_j = (j + floor(return_time)) % m
                    new_mask = mask & ~(1 << i)
                    heappush(heap, (t + return_time, 0, new_mask, new_j))

        return -1.0