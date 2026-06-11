class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        ans = float('inf')
        for i in range(k):
            for j in range(k):
                if i==j:
                    continue
                f = 0
                u,v = 0,0
                for val in nums:
                    x = val%k
                    if f:
                        u+=min(abs(i-x), k-x+i, k-i+x)
                    else:
                        v+=min(abs(j-x), k-x+j, k-j+x)
                    f =1-f
                ans = min(u+v, ans)
        return ans