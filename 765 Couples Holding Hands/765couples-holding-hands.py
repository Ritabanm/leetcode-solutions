class Solution:
    def minSwapsCouples(self, row: list[int]) -> int:

        n = len(row) // 2
        idx = {v: i for i, v in enumerate(row)}
        cnt = 0
        for i in range(0, 2 * n, 2):
            x = row[i]
            y = x ^ 1
            if row[i + 1] != y:
                j = idx[y]
                row[i + 1], row[j] = row[j], row[i + 1]
                idx[row[j]] = j
                idx[row[i + 1]] = i + 1
                cnt += 1
        return cnt