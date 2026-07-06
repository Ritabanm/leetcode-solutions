class Solution:
    def __init__(self):
        self.board = ["abcde", "fghij", "klmno", "pqrst", "uvwxy", "z"]

    def get_coor(self, letter):
        for i, row in enumerate(self.board):
            if letter in row:
                return i, row.index(letter)
            
    def alphabetBoardPath(self, target: str) -> str:
        result = ''
        r1, c1 = self.get_coor('a')
        for char in target:            
            r2, c2 = self.get_coor(char)           
            if c1 > c2:
                result += 'L' * (c1 - c2)
            if r1 < r2:
                result += 'D' * (r2 - r1)
            if r1 > r2:
                result += 'U' * (r1 - r2)                
            if c1 < c2:
                result += 'R' * (c2 - c1)            
            result += '!'
            r1, c1 = r2, c2
        return result
        