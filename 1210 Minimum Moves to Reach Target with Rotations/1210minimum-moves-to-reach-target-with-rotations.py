class Solution:
    def minimumMoves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        seen=set()
        dq=deque()
        dq.append((0,1,"r",0))
        seen.add((0,1,"r"))
        while dq:
            i,j,pos,val=dq.popleft()
            if i==n-1 and j==n-1 and pos=="r": return val 
            #move right
            if j+1<n and grid[i][j+1]==0 and (i,j+1,pos) not in seen:
                if pos=="r" or pos=="d" and grid[i-1][j+1]==0:
                    dq.append((i,j+1,pos,val+1))
                    seen.add((i,j+1,pos))
            #move down
            if i+1<n and grid[i+1][j]==0 and (i+1,j,pos) not in seen:
                if pos=="d" or pos=="r" and grid[i+1][j-1]==0:
                    dq.append((i+1,j,pos,val+1))
                    seen.add((i+1,j,pos))
            #change dir to down if curr is right
            if pos=="r" and j-1>=0 and i+1<n and grid[i+1][j]==grid[i+1][j-1]==0 and (i+1,j-1,"d") not in seen:
                dq.append((i+1,j-1,"d",val+1))
                seen.add((i+1,j-1,"d"))
            #change dir to right if curr is down
            if pos=="d" and i-1>=0 and j+1<n and grid[i-1][j+1]==grid[i][j+1]==0 and (i-1,j+1,"r") not in seen:
                dq.append((i-1,j+1,"r",val+1))
                seen.add((i-1,j+1,"r"))
        return -1