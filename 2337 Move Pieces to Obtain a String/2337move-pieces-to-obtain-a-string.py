class Solution:
    def canChange(self, start: str, target: str) -> bool:
        # Remove blanks and compare the sequence of L and R
        if start.replace("_", "") != target.replace("_", ""):
            return False
        
        # Pointers for both strings
        i, j = 0, 0
        while i < len(start) and j < len(target):
            # Skip blank spaces in `start`
            while i < len(start) and start[i] == "_":
                i += 1
            # Skip blank spaces in `target`
            while j < len(target) and target[j] == "_":
                j += 1
            
            # If both pointers are still within bounds
            if i < len(start) and j < len(target):
                # Ensure the characters are the same
                if start[i] != target[j]:
                    return False
                # Apply movement rules
                if start[i] == "L" and i < j:  # `L` can only move left
                    return False
                if start[i] == "R" and i > j:  # `R` can only move right
                    return False
                # Move to the next characters
                i += 1
                j += 1
        
        # Ensure no leftover characters exist
        while i < len(start) and start[i] == "_":
            i += 1
        while j < len(target) and target[j] == "_":
            j += 1
        
        return i == len(start) and j == len(target)
