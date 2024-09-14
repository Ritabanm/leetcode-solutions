class NeighborSum:

    def __init__(self, grid: list[list[int]]):
        self.grid = grid
        from collections import defaultdict
        self.coords = defaultdict(list)
        rowId = 0
        for row in grid:
            for val in row:
                self.coords[val] = [rowId,row.index(val)]
            rowId += 1
        

    def adjacentSum(self, value: int) -> int:
        Sum = 0
        valCoords = self.coords[value]
        if valCoords[0] > 0: #up
            Sum += self.grid[valCoords[0]-1][valCoords[1]]
        if valCoords[0] < len(self.grid)-1:#down
            Sum += self.grid[valCoords[0]+1][valCoords[1]]
        if valCoords[1] > 0: #left
            Sum += self.grid[valCoords[0]][valCoords[1]-1]
        if valCoords[1] < len(self.grid)-1: #right
            Sum += self.grid[valCoords[0]][valCoords[1]+1]
        return Sum
        
    def diagonalSum(self, value: int) -> int:
        Sum = 0
        valCoords = self.coords[value]
        if valCoords[0] > 0 and valCoords[1] > 0: #up left
            Sum += self.grid[valCoords[0]-1][valCoords[1]-1]
        if valCoords[0] > 0 and valCoords[1] < len(self.grid)-1:#up right
            Sum += self.grid[valCoords[0]-1][valCoords[1]+1]
        if valCoords[0] < len(self.grid)-1 and valCoords[1] > 0: #down left
            Sum += self.grid[valCoords[0]+1][valCoords[1]-1]
        if valCoords[0] < len(self.grid)-1 and valCoords[1] < len(self.grid)-1: #down right
            Sum += self.grid[valCoords[0]+1][valCoords[1]+1]
        return Sum