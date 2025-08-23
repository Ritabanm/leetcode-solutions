class Solution:
    def sumOfPower(self, nums: List[int], k: int) -> int:
        n = len(nums)

        ans = [0 for _ in range(k+1)]
        ans[0] = (1<<n)
        for i in range(n)[::-1]:
            cur = [0 for _ in range(k+1)]
            cur[0] = (1<<n)
            for s in range(1,k+1):
                cur[s] = ans[s]
                if s >= nums[i]:
                    cur[s] += ans[s-nums[i]] // 2

            ans = cur[:]
            
        mm = 10 ** 9 + 7
        return ans[k] % mm
        