class Solution:
    def minimumOperations(self, grid: List[List[int]]) -> int:

        def sm(row: List[int])-> int:
            init = sum(row)

            for i in range(1, len(row)):
                row[i] = max(row[i], row[i-1] + 1)

            return sum(row) - init


        return sum(map(sm, map(list, zip(*grid))))