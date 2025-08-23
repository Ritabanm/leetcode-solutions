class Solution:
    def visibleMountains(self, peaks: List[List[int]]) -> int:
        stack = [-inf]
        curMax = 0
        for x, y in sorted(peaks):
			# find slope
            pos, neg = x-y, x+y 
			
			# remove previous mountain that got overlapped
            while stack[-1] >= pos: stack.pop()
			
			# will not get overlapped by previous mountain
            if neg > curMax: 
                curMax = neg 
                stack.append(pos)
        return len(stack) - 1