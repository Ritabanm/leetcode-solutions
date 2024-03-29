from bisect import bisect_left, bisect_right
from collections import defaultdict

class Solution:
    def numGoodSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        ranks = [0]*n
        r = 0
        for i in range(n):
            if i and nums[i] != nums[i-1]:
                r += 1
            ranks[i] = r
        arr = list(range(n))
        tmp = [0]*n
        itK = 1
        while True:
            sec = [ranks[i+itK] if i+itK < n else -1 for i in range(n)]
            arr.sort(key=lambda i: ranks[i]*(n + 1) + (sec[i] + 1))
            tmp[arr[0]] = 0
            for j in range(1, n):
                a, b = arr[j-1], arr[j]
                tmp[b] = tmp[a] + (ranks[a] != ranks[b] or sec[a] != sec[b])
            ranks, tmp = tmp, ranks
            if ranks[arr[-1]] == n - 1:
                break
            itK <<= 1
        rankpos = [0]*n
        for i, p in enumerate(arr):
            rankpos[p] = i
        lcp = [0]*n
        h = 0
        for i in range(n):
            t = rankpos[i]
            if t == 0:
                h = 0
                continue
            j = arr[t - 1]
            while i + h < n and j + h < n and nums[i + h] == nums[j + h]:
                h += 1
            lcp[t] = h
            if h:
                h -= 1
        prefix = [0]*(n+1)
        for i in range(n):
            prefix[i+1] = (prefix[i] + nums[i]) % k
        pos = defaultdict(list)
        for i, v in enumerate(prefix):
            pos[v].append(i)
        ans = 0
        for t in range(n):
            i = arr[t]
            low = i + lcp[t] + 1
            if low <= n:
                lst = pos[prefix[i]]
                ans += bisect_right(lst, n) - bisect_left(lst, low)
        return ans