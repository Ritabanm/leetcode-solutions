from typing import List

class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        # Track numbers in rows, columns, and boxes using sets
        rows = [set() for _ in range(9)]
        cols = [set() for _ in range(9)]
        boxes = [set() for _ in range(9)]
        empty_cells = []

        # Preprocess board and track empty cells
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    empty_cells.append((i, j))
                else:
                    num = int(board[i][j])
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[(i // 3) * 3 + (j // 3)].add(num)
        
        def backtrack(index):
            if index == len(empty_cells):  # If all empty cells are filled, we're done
                return True

            i, j = empty_cells[index]  # Get next empty cell
            box_index = (i // 3) * 3 + (j // 3)

            for num in range(1, 10):  # Try numbers 1-9
                if num not in rows[i] and num not in cols[j] and num not in boxes[box_index]:
                    # Place the number
                    board[i][j] = str(num)
                    rows[i].add(num)
                    cols[j].add(num)
                    boxes[box_index].add(num)

                    # Recursively attempt to solve the rest
                    if backtrack(index + 1):
                        return True

                    # Undo placement (backtrack)
                    board[i][j] = '.'
                    rows[i].remove(num)
                    cols[j].remove(num)
                    boxes[box_index].remove(num)

            return False  # No valid number found, trigger backtracking
        
        backtrack(0)  # Start solving from the first empty cell
