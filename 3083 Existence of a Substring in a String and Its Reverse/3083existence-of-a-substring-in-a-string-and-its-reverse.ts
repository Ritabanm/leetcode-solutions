function isSubstringPresent(s: string): boolean {
    // initialize new Set()
    let set = new Set();

    // run for loop from index 0
    for (let i = 0; i < s.length - 1; i++) {

        // if ith character and i+1th characters are equal 
        // or set has i+1th and ith character then return true
        if (s[i] === s[i + 1] || set.has(`${s[i + 1]}${s[i]}`)) return true;

        // add ith and i+1th character property in set
        set.add(`${s[i]}${s[i + 1]}`)
    }

    //otherwise return answer false
    return false;
};