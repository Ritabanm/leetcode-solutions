function lastVisitedIntegers(nums: number[]): number[] {
    let seen = []
    let ans = []
    let k = 0;
    for(let i = 0; i < nums.length; i++) {
        if(nums[i] === -1) {
            k++;
            if(k > seen.length) ans.push(-1)
            else ans.push(seen[k - 1])
        } else {
            seen.unshift(nums[i])
            k = 0;
        }
    }
    
    return ans
};