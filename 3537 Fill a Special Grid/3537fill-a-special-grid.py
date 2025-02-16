class Solution:
    def specialGrid(self, N: int) -> List[List[int]]:
        maxm=4**N
        n=2**N
        mat=[[-1]*n for _ in range(n)]
        mat[0][n-1]=0
        ptr=1
        for i in range(N):
            tmp=4**i
            for j in range(ptr):
                for k in range(n-ptr,n):
                    mat[j][k-ptr]=mat[j][k]+3*tmp
                    mat[j+ptr][k]=mat[j][k]+tmp
                    mat[j+ptr][k-ptr]=mat[j][k]+2*tmp
            ptr*=2
        return mat
                    