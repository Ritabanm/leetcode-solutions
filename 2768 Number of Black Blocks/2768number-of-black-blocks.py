class Solution:
    def countBlackBlocks(self, m: int, n: int, coordinates: List[List[int]]) -> List[int]:
        lis=[0 for i in range(5)]
        coordinates={(p[0],p[1]) for p in coordinates}
        augmented_coor=set()
        for c in coordinates:
            augmented_coor.update([(c[0]+d[0],c[1]+d[1]) for d in [[0,-1],[-1,0],[-1,-1],[0,0]] if c[0]+d[0]>=0 and c[0]+d[0]<m and c[1]+d[1]>=0 and c[1]+d[1]<n])

        for p in augmented_coor:
            if p[0]==m-1 or p[1]==n-1: continue
            blacks_in_block=sum([1 for d in [[0,0],[0,1],[1,0],[1,1]] if (d[0]+p[0], d[1]+p[1]) in coordinates])
            lis[blacks_in_block]+=1

        lis[0]=(m-1)*(n-1)-sum(lis[1:])
        return lis