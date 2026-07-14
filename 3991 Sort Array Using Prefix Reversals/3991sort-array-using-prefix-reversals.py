class Solution:
    def sortArray(self, nums: List[int], pre: List[int]) -> int:
        from collections import deque
        target_nums = sorted(nums)
        vis = set()
        vis.add(tuple(nums))
        ans = deque()
        ans.append([nums, 0])
        while ans:
            a,c = ans.popleft()
            if a==target_nums:
                return c
            
            for x in pre:
                na = a[:x][::-1] + a[x:]
                if tuple(na) not in vis:
                    ans.append([na, c+1])
                    vis.add(tuple(na))
        return -1