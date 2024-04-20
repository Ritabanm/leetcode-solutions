function hasTrailingZeros(nums: number[]): boolean {
    let numOfEvens = 0;

    for(let num of nums) {
        if(num % 2 === 0) numOfEvens++;
        
    }

    return numOfEvens > 1;
};