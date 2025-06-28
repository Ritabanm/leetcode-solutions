class Solution:
    def minSwaps(self, grid: List[List[int]]) -> int:
        arr = []
        for row in grid:
            total = 0
            for i in range(len(row)-1,-1,-1):
                if row[i] == 1: break
                total += 1
            
            arr.append(total)

        left = []
        res = 0

        for i in range(len(grid)-1):
            target = len(grid)-1-i
            index = float("inf")
            temp = []
            
            for j in range(len(arr)):
                if arr[j] >= target:
                    index = j
                    break
            
            if index == float("inf"):return -1

            for j in range(len(arr)):
                if j != index:
                    temp.append(arr[j])
            
            left.append(arr[index])
            arr = temp
            res += index
        
        return res
            