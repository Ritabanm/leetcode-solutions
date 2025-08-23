class Solution:
    def maxValue(self, nums: List[int], k: int) -> int:
        self.nums = nums
        n, ans = len(nums), 0
        for i in range(1, n+1):
            for val1 in self.dp1(i, k):
                for val2 in self.dp2(i,k):
                    ans = max(val1^val2, ans)
            # for j in range(k):
            #     del self.dp1(i-2, j)
            
        return ans

    @lru_cache(maxsize=2000)
    def dp1(self, n, k):

        # base condition
        if n<k:
            # print(f"self.dp1({n}, {k})= []")
            return set()
        
        if k==1:
            # print(f"self.dp1({n}, {k})= {set(self.nums[:n])}")

            return set(self.nums[:n])

        ans = set()
        for val in self.dp1(n-1, k-1):
            ans.add(val | self.nums[n-1])
        for val in self.dp1(n-1, k):
            ans.add(val)
        # print(f"self.dp1({n}, {k})={ans}")
        
        return ans

    @lru_cache(maxsize=2000)
    def dp2(self, m, k):
        # base condition
        n = len(self.nums)
        if k> n- m:
            # print(f"self.dp2({m}, {k})= []")
            return set()
        
        if k==1:
            # print(f"self.dp2({m}, {k})= {set(self.nums[m:])}")
            return set(self.nums[m:])

        ans = set()

        for val in self.dp2(m+1, k-1):
            ans.add(val | self.nums[m])
        for val in self.dp2(m+1, k):
            ans.add(val)
        # print(f"self.dp2({m}, {k})={ans}")
        
        return ans