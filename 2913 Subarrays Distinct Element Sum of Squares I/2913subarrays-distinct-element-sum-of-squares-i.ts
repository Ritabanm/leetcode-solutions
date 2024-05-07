function sumCounts(nums: number[]): number {
     const ans: number[] = [];

    ans.push(nums.length * 1);

    for (let i = 0; i < nums.length - 1; i++) {
      for (let j = i + 1; j < nums.length; j++) {
        const cut = nums.slice(i, j + 1);
        
        const uniq = new Set(cut).size;
        ans.push(Math.pow(uniq, 2));
      }
    }
 
    return ans.reduce((a, b) => a + b, 0);
};