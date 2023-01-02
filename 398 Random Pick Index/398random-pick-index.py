import random
from collections import defaultdict

class Solution:

    def __init__(self, nums: List[int]):
        # Preprocess the array and store indices of each number in a dictionary
        self.index_map = defaultdict(list)
        for i, num in enumerate(nums):
            self.index_map[num].append(i)

    def pick(self, target: int) -> int:
        # Retrieve the list of indices for the target and return a random one
        return random.choice(self.index_map[target])
