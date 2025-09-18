function addedInteger(nums1: number[], nums2: number[]): number {
    const n1 = Math.min(...nums1)
    const n2 = Math.min(...nums2)
    return n2 - n1
};