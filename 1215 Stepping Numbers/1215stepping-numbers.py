class Solution:
    def countSteppingNumbers(self, low: int, high: int) -> List[int]:
        q = collections.deque([i+1 for i in range(9)])
        ans = []
        while q and q[0] <= high:
            cur = q.popleft()
            if low <= cur <= high: ans.append(cur)
            m = cur % 10     
            a, b = cur * 10 + (m-1), cur * 10 + (m+1)
            if m != 0: q.append(a)
            if m != 9: q.append(b)
        return [0] + ans if low <= 0 <= high else ans        