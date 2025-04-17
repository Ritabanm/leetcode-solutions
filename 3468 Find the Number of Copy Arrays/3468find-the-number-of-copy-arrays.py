class Solution:
    def countArrays(self, original: List[int], 
                          bounds: List[List[int]]) -> int:

        left, rght = bounds[0]
        shifts = [orig - original[0] for orig in original]

        for (leftBound, rghtBound), shift in zip(bounds, shifts):
            
            leftBound-= shift
            rghtBound-= shift

            left, rght = max(left, leftBound), min(rght, rghtBound)

            if left > rght: return 0 

        return rght+1 - left