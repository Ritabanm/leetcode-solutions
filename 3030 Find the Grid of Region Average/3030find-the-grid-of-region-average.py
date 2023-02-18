class Solution:
    def resultGrid(self, image: List[List[int]], threshold: int) -> List[List[int]]:
        m, n = len(image), len(image[0])
        res = [[0 for _ in range(n)] for _ in range(m)]
        cnt = [[0 for _ in range(n)] for _ in range(m)]
        def isValid(x, y):
            for dx in [-1, 1]:
                for dy in [-1, 1]:
                    if not (abs(image[x][y] - image[x+dx][y]) <= threshold and abs(image[x][y] - image[x][y+dy]) <= threshold):
                        return False
            if not (abs(image[x-1][y-1] - image[x-1][y]) <= threshold and abs(image[x-1][y-1] - image[x][y-1]) <= threshold):
                return False
            if not (abs(image[x-1][y+1] - image[x-1][y]) <= threshold and abs(image[x-1][y+1] - image[x][y+1]) <= threshold):
                return False
            if not (abs(image[x+1][y-1] - image[x+1][y]) <= threshold and abs(image[x+1][y-1] - image[x][y-1]) <= threshold):
                return False
            if not (abs(image[x+1][y+1] - image[x+1][y]) <= threshold and abs(image[x+1][y+1] - image[x][y+1]) <= threshold):
                return False
            return True
            
        for i in range(1, m-1):
            for j in range(1, n-1):
                if isValid(i, j):
                    val = 0
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            cnt[i+dx][j+dy] += 1
                            val += image[i+dx][j+dy]
                    for dx in [-1, 0, 1]:
                        for dy in [-1, 0, 1]:
                            res[i+dx][j+dy] += val // 9
                
                
        for i in range(m):
            for j in range(n):
                if cnt[i][j] == 0:
                    res[i][j] = image[i][j]
                else:
                    res[i][j] //= cnt[i][j]
        
        return res