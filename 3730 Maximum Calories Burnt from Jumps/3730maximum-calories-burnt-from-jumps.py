class Solution:
    def maxCaloriesBurnt(self,heights):
        heights.sort()
        i,j = 0, len(heights)-1
        ans, incr = heights[-1]*heights[-1], False
        while i<j:
            ans+=(heights[i]-heights[j])*(heights[i]-heights[j])
            if incr:
                i+=1
            else:
                j-=1
            incr = not incr
        return ans