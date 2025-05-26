class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        odd, even = Counter(), Counter()
        for i, x in enumerate(nums): 
            if i&1: odd[x] += 1
            else: even[x] += 1
        
        def fn(freq): 
            key = None
            m0 = m1 = 0
            for k, v in freq.items(): 
                if v > m0: key, m0, m1 = k, v, m0
                elif v > m1: m1 = v
            return key, m0, m1
        
        k0, m00, m01 = fn(even)
        k1, m10, m11 = fn(odd)
        return len(nums) - max(m00 + m11, m01 + m10) if k0 == k1 else len(nums) - m00 - m10