function findIndices(nums: number[], indexDifference: number, valueDifference: number): number[] {
    let result: number[] = [];
    for (let i = 0; i < nums.length ; i++) {
        for (let j = i; j < nums.length; j++) {
            if (Math.abs(i - j) >= indexDifference && Math.abs(nums[i] - nums[j]) >= valueDifference) {
                result.push(i, j);
                break;
            }
        }
    }
    if (result.length > 0) return result
    else return [-1, -1]
};