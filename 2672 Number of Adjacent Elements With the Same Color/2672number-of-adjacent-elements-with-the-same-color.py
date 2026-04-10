class Solution:
    def colorTheArray(self, n: int, queries: List[List[int]]) -> List[int]:
        colors = [0] * n
        count = 0
        result = []
        
        for idx, color in queries:
            # Check left neighbor
            if idx > 0 and colors[idx] != 0:
                if colors[idx - 1] == colors[idx]:
                    count -= 1  # this pair was matching, will break
            
            # Check right neighbor
            if idx < n - 1 and colors[idx] != 0:
                if colors[idx + 1] == colors[idx]:
                    count -= 1  # this pair was matching, will break
            
            # Apply the color
            colors[idx] = color
            
            # Check left neighbor again with new color
            if idx > 0 and colors[idx - 1] == colors[idx]:
                count += 1
            
            # Check right neighbor again with new color
            if idx < n - 1 and colors[idx + 1] == colors[idx]:
                count += 1
            
            result.append(count)
        
        return result
