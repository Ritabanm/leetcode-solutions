class Solution:
    def canThreePartsEqualSum(self, arr: List[int]) -> bool:
        s = sum(arr)
        if s % 3:
            return False
        
        part_sum = s / 3
        
        cur_sum = parts = 0
        for num in arr:
            cur_sum += num
            if cur_sum == part_sum:
                if parts == 2:
                    return True
                cur_sum = 0
                parts += 1
        
        return False