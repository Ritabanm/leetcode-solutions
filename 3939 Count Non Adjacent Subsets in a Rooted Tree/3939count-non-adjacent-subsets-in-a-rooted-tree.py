class Solution:
    def countValidSubsets(self, parent: list[int], nums: list[int], k: int) -> int:
        mod = 10**9 + 7
        n = len(parent)
        
        dp0 = [[0] * k for _ in range(n)]
        dp1 = [[0] * k for _ in range(n)]
        
        for i in range(n):
            dp0[i][0] = 1
            dp1[i][nums[i] % k] = 1
            
        for i in range(n - 1, 0, -1):
            p = parent[i]
            
            nxt_dp0 = [0] * k
            nxt_dp1 = [0] * k
            
            child_any = [(dp0[i][r] + dp1[i][r]) % mod for r in range(k)]
                
            for r_p in range(k):
                if dp0[p][r_p]:
                    for r_c in range(k):
                        if child_any[r_c]:
                            nxt_rem = (r_p + r_c) % k
                            nxt_dp0[nxt_rem] = (nxt_dp0[nxt_rem] + dp0[p][r_p] * child_any[r_c]) % mod
                            
                if dp1[p][r_p]:
                    for r_c in range(k):
                        if dp0[i][r_c]:
                            nxt_rem = (r_p + r_c) % k
                            nxt_dp1[nxt_rem] = (nxt_dp1[nxt_rem] + dp1[p][r_p] * dp0[i][r_c]) % mod
                            
            dp0[p] = nxt_dp0
            dp1[p] = nxt_dp1
            
        ans = (dp0[0][0] + dp1[0][0] - 1) % mod
        return ans