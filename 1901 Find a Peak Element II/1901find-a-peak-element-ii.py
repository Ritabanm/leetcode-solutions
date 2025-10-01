class Solution:
    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        hu=[]
        jk=[]
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                hu.append(mat[i][j])
        x=max(hu)
        print(x)
        for i in range(len(mat)):
            for j in range(len(mat[i])):
                if(mat[i][j]==x):
                    jk.append(i)
                    jk.append(j)
            if(len(jk)==2):
                break
        return jk