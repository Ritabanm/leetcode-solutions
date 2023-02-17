function satisfiesConditions(grid: number[][]): boolean {
    for(let indexRow=0; indexRow<grid.length; indexRow++){
        for(let indexCol=0; indexCol<grid[0].length; indexCol++){
            // DO NOT consider cell below check on last row
            if(indexRow !== grid.length-1){
                if(grid[indexRow][indexCol] !== grid[indexRow+1][indexCol]) return false;
            }

            // DO NOT consider cell right check on last column
            if(indexCol !== grid[0].length-1){
                if(grid[indexRow][indexCol] === grid[indexRow][indexCol+1]) return false;
            }
        }
    }

    return true;
};