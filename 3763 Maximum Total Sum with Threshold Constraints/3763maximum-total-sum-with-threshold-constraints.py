class Solution:
    def maxSum(self, nums: List[int], threshold: List[int]) -> int:
        ans = 0
        step = 1
        sl = SortedList()
        for i, n in enumerate(nums):
            sl.add((threshold[i], -n))
        #print(sl)
        used = set()
        for i in range(len(nums)):
            #print(step, sl, ans)
            flag = False
            for j, n in enumerate(sl):
                if n[0] <= step:
                    flag = True
                    #print(n)
                    ans += abs(n[1])
                    del sl[j]
                    break
            if not flag: return ans
            step += 1
        return ans