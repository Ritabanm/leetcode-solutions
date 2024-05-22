class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        from collections import defaultdict
        
        # Store the list of indices for each number
        indices = defaultdict(list)
        for idx, num in enumerate(nums):
            indices[num].append(idx)
            
        special_count = 0
        
        for num, idx_list in indices.items():
            # Must appear at least 3 times
            if len(idx_list) >= 3:
                # Calculate the gap between the first two occurrences
                common_diff = idx_list[1] - idx_list[0]
                is_special = True
                
                # Check if all subsequent gaps match the first gap
                for i in range(2, len(idx_list)):
                    if idx_list[i] - idx_list[i - 1] != common_diff:
                        is_special = False
                        break
                        
                if is_special:
                    special_count += 1
                    
        return special_count