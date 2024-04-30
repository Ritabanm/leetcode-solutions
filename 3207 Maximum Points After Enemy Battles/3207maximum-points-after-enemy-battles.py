class Solution:
    def maximumPoints(self, enemyEnergies: List[int], currentEnergy: int) -> int:
        enemyEnergies.sort()
        if currentEnergy < enemyEnergies[0]: return 0
        totalEnergy = currentEnergy
        for j in range(len(enemyEnergies) - 1, 0, -1): totalEnergy += enemyEnergies[j]
        return totalEnergy // enemyEnergies[0]