from collections import defaultdict

class Solution:
    def countPalindromePaths(self, parent: List[int], s: str) -> int:
        n = len(parent)
        
        # Build adjacency list
        children = defaultdict(list)
        for i in range(1, n):
            children[parent[i]].append(i)
        
        result = 0
        # mask_count[mask] = number of nodes seen with this XOR mask from root
        mask_count = defaultdict(int)
        mask_count[0] = 1  # root has mask 0
        
        # Iterative DFS with (node, current_mask)
        stack = [(0, 0)]
        while stack:
            node, mask = stack.pop()
            
            for child in children[node]:
                # XOR with the edge character
                new_mask = mask ^ (1 << (ord(s[child]) - ord('a')))
                
                # Count valid pairs: new_mask ^ existing == 0 or power of 2
                result += mask_count[new_mask]  # exact match (XOR = 0)
                for bit in range(26):            # one bit different (XOR = power of 2)
                    result += mask_count[new_mask ^ (1 << bit)]
                
                mask_count[new_mask] += 1
                stack.append((child, new_mask))
        
        return result
