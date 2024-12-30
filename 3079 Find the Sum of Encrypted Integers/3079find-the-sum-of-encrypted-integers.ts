function sumOfEncryptedInt(nums: number[]): number {
    let result = 0;
    for (const num of nums) {
        let max = 1;
        let numS = num.toString();
        let multi = 0;
        for (let i = 0; i < numS.length; i++) {
            multi += 10 ** i;
            if (Number(numS[i]) > max) max = Number(numS[i]);
        }
        result += max * multi;
    }
    return result;
}