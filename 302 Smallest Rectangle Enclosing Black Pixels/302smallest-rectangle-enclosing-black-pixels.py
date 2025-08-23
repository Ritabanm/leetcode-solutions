from typing import List
from bisect import bisect_left, bisect_right


class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if not image: return 0  # Early return for empty image

        m, n = len(image), len(image[0])
        # why need four functions the search space has to be sorted which means it should be
        # [F,F,F,T,T,T] and not [T,T,T,F,F,F] for binary search to work the 
        # search space before (x, y) looks like [F,F,F,T,T,T] and we want find the left most True
        # search space after  (x, y) looks like [F,F,F,T,T,T] and we want find the right most False

        def check_col_left(mid): return any(image[i][mid] == '1' for i in range(m)) 
        def check_col_right(mid): return all(image[i][mid] == '0' for i in range(m))

        def check_row_top(mid): return any(image[mid][j] == '1' for j in range(n))
        def check_row_bottom(mid): return all(image[mid][j] == '0' for j in range(n))

        left = bisect_left(range(y+1), True, key=check_col_left)
        right = y + bisect_right(range(y, n), False, key=check_col_right)

        top = bisect_left(range(x+1), True, key=check_row_top)
        bottom = x + bisect_right(range(x, m), False, key=check_row_bottom)

        # print(left, right)
        # print(top, bottom)

        return (right - left) * (bottom - top)