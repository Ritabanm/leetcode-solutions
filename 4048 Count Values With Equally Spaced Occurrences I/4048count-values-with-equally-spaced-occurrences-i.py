class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        from collections import defaultdict
        indices = defaultdict(list)
        for idx,num in enumerate(nums):
            indices[num].append(idx)
        special_count = 0
        for num, idx_list in indices.items():
            if len(idx_list)==3:
                i1,i2,i3 = idx_list
                if i2-i1 == i3-i2:
                    special_count+=1
        return special_count
        #T:O(N), S:O(N)