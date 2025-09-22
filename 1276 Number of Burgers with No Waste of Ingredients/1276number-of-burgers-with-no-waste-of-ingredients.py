class Solution:
    def numOfBurgers(self, tomatoSlices: int, cheeseSlices: int) -> List[int]:
        unused = tomatoSlices - (cheeseSlices*2)
        if unused<0 or unused%2:
            return []
        jumbos = unused//2
        if jumbos>cheeseSlices:
            return []

        small = cheeseSlices-jumbos
        return [jumbos, small]