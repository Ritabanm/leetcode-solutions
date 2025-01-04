class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        from collections import Counter
        
        # Store all rows as tuples in a Counter
        row_counter = Counter(tuple(row) for row in grid)
        
        # Initialize the count of matching pairs
        count = 0
        
        # Iterate over columns
        for col_index in range(len(grid[0])):
            # Extract the column as a tuple
            column = tuple(grid[row][col_index] for row in range(len(grid)))
            
            # Add the number of rows that match this column
            count += row_counter[column]
        
        return count
