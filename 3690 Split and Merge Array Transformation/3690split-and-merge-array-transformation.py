class Solution:
    def minSplitMerge(self, nums1: List[int], nums2: List[int]) -> int:
        q = deque()
        n = len(nums1)
        q.append((nums1, 0))
        vis = set()
        while q:
            ne, steps = q.popleft()
            ne = list(ne)
            if ne == nums2:
                return steps
            for i in range(n):
                for j in range(i + 1, n):
                    x = ne[i : j]
                    size = n - (j - i)
                    temp = ne[:i] + ne[j:]
                    for k in range(n):
                        newl = tuple(temp[:k] + x + temp[k:])
                        if newl not in vis:
                            vis.add(newl)
                            q.append((newl,steps + 1))