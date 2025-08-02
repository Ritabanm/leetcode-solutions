class Solution:
    def trap(self, height):

        #Edge case: height is empty
        if not height or len(height)==0:
            return 0
        
        #variables:
        l = 0
        r = len(height)-1 
        lmax = 0
        rmax = 0
        ans = 0

        while l<r:
            if height[l]<height[r]:
                lmax = max(lmax, height[l])
                ans+=lmax-height[l]
                l+=1
            else:
                rmax = max(rmax, height[r])
                ans+=rmax-height[r]
                r-=1
        return ans

        #T: O(N), S:O(1)