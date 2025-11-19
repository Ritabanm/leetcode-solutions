class Solution:
    def elementInNums(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        time = []
        out = []
        for i in range(len(nums)*2):
            if i<len(nums):
                minu = nums[i:]
            else:
                minu = nums[:(i-len(nums))]
            time.append(minu)

        for j in queries:
            try:
                out.append(time[j[0]%len(time)][j[1]])
            except:
                out.append(-1)
        return out