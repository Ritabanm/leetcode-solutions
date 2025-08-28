from typing import List
from collections import deque

class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        def isValid(string):
            count = 0
            for char in string:
                if char == "(":
                    count += 1
                elif char == ")":
                    count -= 1
                if count < 0:
                    return False  # More ')' than '('
            return count == 0  # Ensure equal '(' and ')'

        # BFS queue to explore different removals
        queue = deque([s])
        visited = set([s])
        valid_results = []
        found = False

        while queue:
            curr_string = queue.popleft()
            
            if isValid(curr_string):
                valid_results.append(curr_string)
                found = True  # Once we find valid strings, stop further removals
            
            if found:
                continue  # No further processing once we find the first valid level

            for i in range(len(curr_string)):
                if curr_string[i] not in "()":
                    continue  # Skip non-parentheses

                # Remove the i-th character and check new string
                new_string = curr_string[:i] + curr_string[i+1:]
                if new_string not in visited:
                    visited.add(new_string)
                    queue.append(new_string)

        return valid_results if valid_results else [""]
