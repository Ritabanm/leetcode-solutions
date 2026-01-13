class Solution:
    def countLatticePoints(self, circles: List[List[int]]) -> int:
        res=[]
        for cirlcle in circles:
            x=cirlcle[0]
            y= cirlcle[1]
            rad = cirlcle[2]
            for x1 in range(x-rad,x+rad+1):
                for y1 in range(y-rad,y+rad+1):
                    if((x-x1)*(x-x1)+(y-y1)*(y-y1))<=rad*rad:
                            res.append((x1,y1))
        mylist=list(set(res))
        return len(mylist)
    