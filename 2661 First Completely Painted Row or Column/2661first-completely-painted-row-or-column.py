class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        rows, cols = len(mat), len(mat[0])
        mat_to_position = {}
        for r in range(rows):
            for c in range(cols):
                mat_to_position[mat[r][c]] = (r,c)
        row_cnt = [0]*rows
        col_cnt = [0]*cols
        for i in range(len(arr)):
            r,c = mat_to_position[arr[i]]
            row_cnt[r] +=1
            col_cnt[c] +=1
            if col_cnt[c] == rows or row_cnt[r] == cols:
                return i