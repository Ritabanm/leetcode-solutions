class Solution:
    def getMinDistSum(self, positions):
        def dist(x,y):
            return sum([math.sqrt((x-a)**2 + (y-b)**2) for a,b in positions])

        x,y = sum([i[0] for i in positions])/len(positions), sum([i[1] for i in positions])/len(positions)
        step = 100

        while step > 1e-6:
            for dx,dy in [[0,1],[0,-1],[1,0],[-1,0]]:
                nx,ny = x+step*dx,y+step*dy
                if dist(nx,ny) < dist(x,y):
                    x,y = nx,ny
                    break
            else:
                step = step/2

        return dist(x,y)

        






        

        




        