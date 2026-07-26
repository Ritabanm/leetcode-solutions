class Solution:
    def totalScore(self, hp: int, damage: List[int], requirement: List[int]) -> int:
        N = len(damage)
        prefixDamage = [0]*(N+1)
        for index in range(1,N+1):
            prefixDamage[index]=prefixDamage[index-1] + damage[index-1]
        totalScore = 0
        for j in range(N):
            requiredPrefix = requirement[j] + prefixDamage[j+1]-hp
            i = bisect.bisect_left(prefixDamage, requiredPrefix,0,j+1)
            totalScore += (j+1-i)
        return totalScore