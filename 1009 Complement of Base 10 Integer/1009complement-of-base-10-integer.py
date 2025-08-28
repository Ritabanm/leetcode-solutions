class Solution:
    def bitwiseComplement(self, n: int) -> int:
        if n == 0:
            return 1
        
        todo, bit = n, 1
        while todo:
        # Flip the current bit
            n = n^bit
        # prepare for the next run 
            bit  = bit<<1
            todo = todo>>1
        
        return n