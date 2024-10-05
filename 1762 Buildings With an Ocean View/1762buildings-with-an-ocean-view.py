class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        max_height = -1
        res = collections.deque([])
        for i in range(len(heights)-1, -1,-1):
            cur_height = heights[i]
            if cur_height>max_height:
                res.appendleft(i)
                max_height=cur_height
        return res