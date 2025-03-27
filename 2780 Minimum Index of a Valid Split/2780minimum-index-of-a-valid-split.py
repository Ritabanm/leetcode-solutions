class Solution:
    def minimumIndex(self, nums:List[int])-> int:
        f_map = defaultdict(int)
        s_map = defaultdict(int)

        n = len(nums)

        for num in nums:
            s_map[num]+=1
        
        for index in range(n):
            num = nums[index]
            s_map[num]-=1
            f_map[num]+=1
            if (f_map[num]*2 > index+1 and s_map[num]*2>n-index-1):
                return index

        return -1