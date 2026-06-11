class Solution:
    def minGenerations(self, points: List[List[int]], target: List[int]) -> int:
        n=len(points)
        if target in points:
            return 0
        if n==1:
            return -1
        queue=deque()
        visited=set()
        for a,b,c in points:
            queue.append((a,b,c,0,len(points)))
            visited.add((a,b,c))
        while(queue):
            curr=queue.popleft() 
            x,y,z,cst,l=curr
            if [x,y,z]==target:
                return cst
            for i in range(0,l):
                a,b,c=points[i]
                nx,ny,nz=(x+a)//2,(y+b)//2,(z+c)//2
                if (nx,ny,nz) not in visited:
                    queue.append((nx,ny,nz,cst+1,len(points)+1))
                    visited.add((nx,ny,nz))
                    points.append([nx,ny,nz])
        return -1
                    
                
                