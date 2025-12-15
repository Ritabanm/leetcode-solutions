class Solution:
    def maxJump(self, stones: List[int]) -> int:
        if len(stones)==2:
            return stones[1]-stones[0]
        
        jump = stones[0]
        for i in range(len(stones)-2):
            jump = max(jump, stones[i+2]-stones[i])
        return jump