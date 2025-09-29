class Solution:
    def digArtifacts(self, n: int, artifacts: List[List[int]], dig: List[List[int]]) -> int:
        '''
        no two artifcats overlap

        we preditermine where you dig


        '''
        A = [[0] * n for _ in range(n)]
        for x, y in dig:
            A[x][y]=1

        ans = 0

        for x1, y1, x2, y2 in artifacts:
            
            good = 1
            for i in range(x1, x2+1):
                for j in range(y1, y2+1):
                    if A[i][j] == 0:
                        good = 0

            ans += good

        return ans