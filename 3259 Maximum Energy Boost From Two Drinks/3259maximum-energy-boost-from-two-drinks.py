class Solution:
    def maxEnergyBoost(self, energyDrinkA: List[int], energyDrinkB: List[int]) -> int:
        
        prev_A = curr_A = prev_B = curr_B = 0

        for a, b in zip(energyDrinkA, energyDrinkB):
            add_A = a + max(curr_A, prev_B)
            add_B = b + max(curr_B, prev_A)

            prev_A, prev_B, curr_A, curr_B = curr_A, curr_B, add_A, add_B

        return max(curr_A, curr_B)