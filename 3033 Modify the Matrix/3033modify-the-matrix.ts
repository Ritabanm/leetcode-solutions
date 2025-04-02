function modifiedMatrix(grid: number[][]): number[][] {
    for (let colIndex = 0; colIndex < grid[0].length; colIndex++) {
        let max = grid[0][colIndex];
        for (let rowIndex = 0; rowIndex < grid.length; rowIndex++) {
            max = Math.max(max, grid[rowIndex][colIndex]);
        }

        for (let rowIndex = 0; rowIndex < grid.length; rowIndex++) {
            if (grid[rowIndex][colIndex] === -1) {
                grid[rowIndex][colIndex] = max;
            }
        }
    }

    return grid;
};