class Solution:
    def winningPlayer(self, x: int, y: int) -> str:
        if x < (y // 4): # 75-coins will run out first
            if x % 2 == 0: # coins run out after an even turn
                return "Bob"
            else:
                return "Alice"
        else: # 10-coins will run out first
            if (y // 4) % 2 == 0: # coins run out after an even turn
                return "Bob"
            else:
                return "Alice"