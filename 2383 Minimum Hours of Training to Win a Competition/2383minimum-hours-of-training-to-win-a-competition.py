from typing import List

class Solution:
    def minNumberOfHours(self, initialEnergy: int, initialExperience: int, energy: List[int], experience: List[int]) -> int:
        # Compute required energy training hours
        training_hours = max(0, sum(energy) - initialEnergy + 1)

        experience_training = 0
        my_exp = initialExperience
        
        for exp in experience:
            if my_exp <= exp:
                experience_training += exp + 1 - my_exp
                my_exp = exp + 1  # Just enough to beat the current opponent
            my_exp += exp  # Gain experience normally
        
        return training_hours + experience_training