class Solution:
    def minInteger(self, num: str, k: int) -> str:
        nums = [int(c) for c in num]
        moves_remaining = k

        start = []
        for digit in range(10):
            non_digits = 0 
            min_seen = 10 # minimum integer seen this round 
            new_nums = [] # not deleted from this round
            for idx, num in enumerate(nums):
                if num == digit:
                    if ((non_digits <= moves_remaining) 
                        # edge case if we have to break here
                        and (digit <= min_seen)): 
                        start.append(num)
                        moves_remaining -= non_digits
                    else:
                        new_nums.append(num)
                else:
                    min_seen = min(min_seen, num)
                    non_digits += 1
                    new_nums.append(num)
            
            nums = new_nums

        # we can't get the number we need to move to the start
        # just look along nums for an unsorted digit, and move it
        
        nums = start + nums

        if moves_remaining > 0:
            current = -1
            for idx, num in enumerate(nums):
                if num < current:
                    target_idx = idx - moves_remaining
                    nums = (
                        nums[:target_idx] 
                        + [num]
                        + nums[target_idx: idx]
                        + nums[idx + 1:]
                    )
                    break
                current = num
        return "".join(str(x) for x in nums)
        
            
