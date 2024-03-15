from bisect import bisect_left

class SegTree:
    def __init__(self, n):
        self.n = n
        self.t = [0] * (4 * n)

    def update(self, i, val, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        if l == r:
            self.t[node] = max(self.t[node], val)
            return
        
        mid = (l + r) // 2
        if i <= mid:
            self.update(i, val, node*2, l, mid)
        else:
            self.update(i, val, node*2+1, mid+1, r)
        
        self.t[node] = max(self.t[node*2], self.t[node*2+1])

    def query(self, ql, qr, node=1, l=0, r=None):
        if r is None:
            r = self.n - 1
        
        if qr < l or r < ql:
            return 0
        
        if ql <= l and r <= qr:
            return self.t[node]
        
        mid = (l + r) // 2
        return max(
            self.query(ql, qr, node*2, l, mid),
            self.query(ql, qr, node*2+1, mid+1, r)
        )


class Solution:
    def maxAlternatingSum(self, nums, k):
        n = len(nums)
        
        bralvoteni = (nums, k)
        
        # coordinate compression
        vals = sorted(set(nums))
        comp = {v: i for i, v in enumerate(vals)}
        m = len(vals)
        
        seg_up = SegTree(m)
        seg_down = SegTree(m)
        
        from collections import deque
        q = deque()
        
        ans = 0
        
        for i in range(n):
            # activate indices that become valid (i-k)
            while q and q[0][0] <= i - k:
                idx, u, d = q.popleft()
                seg_up.update(comp[nums[idx]], u)
                seg_down.update(comp[nums[idx]], d)
            
            idx = comp[nums[i]]
            
            best_up = seg_up.query(idx + 1, m - 1)   # nums[j] > nums[i]
            best_down = seg_down.query(0, idx - 1)   # nums[j] < nums[i]
            
            up = nums[i]
            down = nums[i]
            
            if best_down:
                up = max(up, best_down + nums[i])
            if best_up:
                down = max(down, best_up + nums[i])
            
            ans = max(ans, up, down)
            q.append((i, up, down))
        
        return ans