class Solution:
    def maxRectangleArea(self, xCoordGiven: List[int], yCoordGiven: List[int]) -> int:
        xpt = dict()
        ypt = dict()
        points = list(zip(xCoordGiven,yCoordGiven))
        points.sort(key=itemgetter(1)) # sort the points by y-coordinate
        yCoord = [y for x,y in points]
        
        xset = set()
        yset = set()
        for i,(x,y) in enumerate(points):
            xset.add(x)
            yset.add(y)
            if x not in xpt:
                xpt[x] = [(y,i)]
            else:
                xpt[x].append((y,i))
            if y not in ypt:
                ypt[y] = [(x,i)]
            else:
                ypt[y].append((x,i))
        for x in xset:
            xpt[x].sort()
        for y in yset:
            ypt[y].sort()
            
        numYBuckets = 1
        while (numYBuckets*numYBuckets) < len(points):
            numYBuckets += 1
        yBuckets = [[] for _ in range(numYBuckets)]

        def getYBucketIdx(yval):
            ret = bisect_left(yCoord,yval)
            ret = ret//len(yBuckets)
            return min(ret,len(yBuckets)-1)

        for i,(x,y) in enumerate(points):
            yBuckets[getYBucketIdx(y)].append((x,i))
        for bktIdx in range(numYBuckets):
            yBuckets[bktIdx].sort()
            
        result = -1
        for xLeft,pts in xpt.items():
            # for all the points that lie on x verital line. Sort the y values.

            for i in range(len(pts)-1):
                
                yBottom,bottomLeftIdx = pts[i]
                # now we use the next y as yTop
                yTop,topLeftIdx       = pts[i+1]
                # now we need to find the xRight
                yBottomPts = ypt[yBottom]
                idx = bisect_left(yBottomPts, (xLeft+1,0))
                if idx >= len(yBottomPts):
                    continue
                xRight,bottomRightIdx = yBottomPts[idx]
                yTopPts = ypt[yTop]
                idx = bisect_left(yTopPts, (xLeft+1,0))
                if idx >= len(yTopPts):
                    continue
                xRight2,topRightIdx = yTopPts[idx]
                if xRight != xRight2:
                    continue

                # how many points are between xLeft and xRight ?
                
                # calculate area
                #print(xRight,xLeft,yTop,yBottom)
                # for all the points that lie between xLeft and xRight
                bad = False
                for bktIdx in range(getYBucketIdx(yBottom),getYBucketIdx(yTop)+1):
                    bkt = yBuckets[bktIdx]
                    idx = bisect_left(bkt,(xLeft,0))
                    for j in range(idx,len(bkt)):
                        xx,ii = bkt[j]
                        yy = points[ii][1]
                        if xx > xRight:
                            break
                        if ii in (bottomLeftIdx,bottomRightIdx,topLeftIdx,topRightIdx):
                            continue
                        if xx >= xLeft and xx <= xRight:
                            if yy >= yBottom and yy <= yTop:
                                bad = True
                                break
                if not bad:
                    area = (xRight-xLeft)*(yTop-yBottom)
                    result = max(result,area)
        return result