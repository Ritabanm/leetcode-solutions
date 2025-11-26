function canMakeSquare(grid: string[][]): boolean {
    for (let i = 0; i < 2; i++) {
        for (let j = 0; j < 2; j++) {
            let countW = 0;
            let countB = 0;
            grid[i][j] === "B" ? countB++ : countW++;
            grid[i][j + 1] === "W" ? countW++ : countB++;
            grid[i + 1][j] === "B" ? countB++ : countW++;
            grid[i + 1][j + 1] === "W" ? countW++ : countB++;
            if (countB !== 2) return true;
        }
    }
    return false;
}