from collections import deque
class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        F = pow(2,m) - 1
        que = deque([(num^F,0) for num in nums])
        dist = defaultdict(lambda:float('inf'))
        while que:
            v, d = que.popleft()
            if dist[v] != float('inf'): continue
            dist[v] = d
            for j in range(m):
                que.append((v^(1<<j),d+1))
        return [m - dist[num] for num in nums] 

        