def L(nums,k):
        c=Counter()
        res=[float('inf')]*len(nums)
        l=0
        for r,x in enumerate(nums):            
            c[x]+=1
            while len(c)>k:
                c[nums[l]]-=1
                if c[nums[l]]==0: 
                    del c[nums[l]]
                l+=1
            if len(c)==k:
                res[r]=l
        return res

class Solution:
    def validSubarrays(self, nums: List[int], k: int, l0: int, r0: int, q: int) -> List[bool]:
        xorsum=list(accumulate(nums,operator.xor,initial=0))
        lk=L(nums,k)
        lk1=L(nums,k-1)
        res = []
        l,r = l0,r0
        N = len(nums)
        for i in range(q):
            curr = (r-l+1) % 2 == 0 and xorsum[r+1]==xorsum[l] and lk[r]<=l<lk1[r]
            
            res.append(curr)

            if curr: g = l+r
            else: g = r-l
            l,r = (l^g) % N,(r^g) % N
            l,r = sorted([l,r])
        return res
        
                