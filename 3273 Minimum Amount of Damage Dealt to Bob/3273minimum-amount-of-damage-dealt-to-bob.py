class Solution:
    def minDamage(self, power: int, damage: List[int], health: List[int]) -> int:
        n = len(damage)
        for i in range(n):
            health[i]=(health[i]+power-1)//power
        indexes = sorted(
            range(n), key = cmp_to_key(lambda i,j:health[i]*damage[j]-
            health[j]*damage[i]), 
        )
        res = 0
        curTime = 0
        for i in indexes:
            curTime+=health[i]
            res += curTime*damage[i]
        return res
        