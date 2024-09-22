class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
        dq = collections.deque([x])
        visited = set()
        step = 0
        while dq:
            n = len(dq)
            for _ in range(n):
                v = dq.popleft()
                if v == y: return step
                visited.add(v)
                if v % 11 == 0 and v // 11 not in visited: dq.append(v // 11)
                if v % 5 == 0 and v // 5 not in visited: dq.append(v // 5)
                if v + 1 not in visited: dq.append(v + 1)
                if v - 1 not in visited: dq.append(v - 1)
            step += 1
        
        return -1