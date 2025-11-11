class Solution:
    def countElements(self, arr: List[int]) -> int:
        count = 0
        for x in arr:
            if x+1 in arr:
                count+=1
        return count