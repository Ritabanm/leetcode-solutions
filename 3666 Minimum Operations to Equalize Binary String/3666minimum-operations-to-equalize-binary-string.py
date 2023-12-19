class Solution:
    def minOperations(self, s: str, k: int) -> int:
        z = s.count('0')
        g = math.gcd(2, k)
        if z % g != 0:
            return -1

        N = len(s)
        queue = deque([(z,0)])
        notused_0 = SortedList(range(0,N+1,2))
        notused_1 = SortedList(range(1,N+1,2))
        if z % 2 == 0:
            notused_0.remove(z)
        else:
            notused_1.remove(z)

        while queue:
            zs, step = queue.popleft()
            if zs == 0:
                return step

            mi = max(0, k + zs - N)
            ma = min(k, zs)
            L = zs + k - 2 * ma
            R = zs + k - 2 * mi
            p = L % 2
            if p == 0: 
                i = notused_0.bisect_left(L)
                while i < len(notused_0):
                    newz = notused_0[i]
                    if newz > R:
                        break
                    queue.append((newz, step+1))
                    notused_0.pop(i)
            else:
                i = notused_1.bisect_left(L)
                while i < len(notused_1):
                    newz = notused_1[i]
                    if newz > R:
                        break
                    queue.append((newz, step+1))
                    notused_1.pop(i)
        return -1