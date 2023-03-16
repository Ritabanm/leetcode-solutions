class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        # Dictionary to store computed results
        memo = {}

        def dfs(s1, s2):
            # Check if the result is already computed
            if (s1, s2) in memo:
                return memo[(s1, s2)]

            # Base cases
            if s1 == s2:
                return True
            if sorted(s1) != sorted(s2):  # If they don't have the same characters, return False
                return False

            n = len(s1)
            # Try every possible split
            for i in range(1, n):
                # Case 1: No Swap
                if dfs(s1[:i], s2[:i]) and dfs(s1[i:], s2[i:]):
                    memo[(s1, s2)] = True
                    return True
                
                # Case 2: Swap
                if dfs(s1[:i], s2[-i:]) and dfs(s1[i:], s2[:-i]):
                    memo[(s1, s2)] = True
                    return True
            
            # If no match found, store the result and return False
            memo[(s1, s2)] = False
            return False

        return dfs(s1, s2)
