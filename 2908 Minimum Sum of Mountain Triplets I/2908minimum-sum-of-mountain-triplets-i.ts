function minimumSum(nums: number[]): number {
    const possibleSums: number[] = []
    for (let i = 0; i < nums.length - 2; i++) {
        for (let j = i + 1; j < nums.length - 1; j++) {
            for (let k = j + 1; k < nums.length; k++) {
                if (nums[i] < nums[j] && nums[k] < nums[j])  possibleSums.push(nums[i] + nums[j] + nums[k])
            }
        }
    }
    return possibleSums.length ? Math.min(...possibleSums.map(el => el)) : -1
};