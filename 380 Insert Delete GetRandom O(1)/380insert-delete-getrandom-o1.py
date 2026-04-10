import random

class RandomizedSet:

    def __init__(self):
        self.val_to_idx = {}   # value -> index in list
        self.vals = []         # list of values

    def insert(self, val: int) -> bool:
        if val in self.val_to_idx:
            return False
        self.vals.append(val)
        self.val_to_idx[val] = len(self.vals) - 1
        return True

    def remove(self, val: int) -> bool:
        if val not in self.val_to_idx:
            return False
        # Swap val with the last element
        idx = self.val_to_idx[val]
        last = self.vals[-1]
        self.vals[idx] = last
        self.val_to_idx[last] = idx
        # Remove last element
        self.vals.pop()
        del self.val_to_idx[val]
        return True

    def getRandom(self) -> int:
        return random.choice(self.vals)
