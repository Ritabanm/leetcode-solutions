class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        ones = 0
        index = 0
        for it, row in enumerate(mat):
            c = row.count(1)
            if ones<c:
                ones = c
                index = it
        return [index, ones]