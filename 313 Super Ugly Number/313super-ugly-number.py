import heapq as q

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        queue, visited, x, i = [1], set(), None, 0
        while i < n:
            x = q.heappop(queue)
            if x in visited:
                continue
            visited.add(x)
            i += 1
            for p in primes:
                q.heappush(queue, x * p)
        return x