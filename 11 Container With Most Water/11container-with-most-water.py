"""class Solution:
    def maxArea(self, height):
        maxArea = 0
        l = 0
        r = len(height)-1
        while l<r:
            w = r-l
            maxArea = max(maxArea, min(height[l], height[r])*w)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxArea"""

class Solution:
    def maxArea(self,height):
        maxArea = 0
        l = 0
        r = len(height)-1
        while l<r:
            w = r-l
            maxArea = max(maxArea, min(height[l], height[r])*w)
            if height[l]<=height[r]:
                l+=1
            else:
                r-=1
        return maxArea