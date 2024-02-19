class Solution:
    def longestConsecutive(self,nums):
        ls = 0
        num_set = set(nums)
        for num in num_set:
            if num-1 not in num_set:
                current_num = num
                cs = 1
                while current_num+1 in num_set:
                    current_num+=1
                    cs +=1
                ls = max(ls, cs)
        return ls