class TicTacToe:
    def __init__(self, n: int):
        """
        Initialize the game board.
        n: The size of the board (n x n).
        """
        self.n = n
        self.rows = [0] * n  # Track row counts for each player
        self.cols = [0] * n  # Track column counts for each player
        self.diagonal = 0    # Track main diagonal count for each player
        self.anti_diagonal = 0  # Track anti-diagonal count for each player

    def move(self, row: int, col: int, player: int) -> int:
        """
        Makes a move on the board and checks for a win.
        player: 1 for player 1, -1 for player 2
        row, col: The position on the board where the move is made.
        Returns:
            0 if there is no winner,
            1 if player 1 wins,
            2 if player 2 wins.
        """
        mark = 1 if player == 1 else -1  # Use +1 for player 1, -1 for player 2
        
        # Update the row and column counts
        self.rows[row] += mark
        self.cols[col] += mark
        
        # Update the diagonals if applicable
        if row == col:
            self.diagonal += mark
        
        if row + col == self.n - 1:
            self.anti_diagonal += mark
        
        # Check if the current player wins
        if (abs(self.rows[row]) == self.n or
            abs(self.cols[col]) == self.n or
            abs(self.diagonal) == self.n or
            abs(self.anti_diagonal) == self.n):
            return 1 if player == 1 else 2
        
        # If no one wins, return 0
        return 0
