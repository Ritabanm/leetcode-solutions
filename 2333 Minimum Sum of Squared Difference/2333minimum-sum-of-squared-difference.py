class Solution:
    def minSumSquareDiff(self, nums1: List[int], nums2: List[int], k1: int, k2: int) -> int:
        diff = [abs(nums1[i]-nums2[i]) for i in range(len(nums1))]
        bucket = Counter(diff)
        M = max(diff)
        k = k1+k2
        for j in reversed(range(1,M+1)):
            minus = min(k,bucket[j])
            bucket[j]-=minus
            bucket[j-1]+=minus
            k-=minus
            if k == 0:
                break
        return sum([count*(d**2) for d,count in bucket.items()])