class Robot:

    def __init__(self, width: int, height: int):
        self.width = width - 1
        self.height = height - 1
        self.curr_loc = [0,0]
        self.allowed_dir = {
            'e': 'East', # w
            'n': 'North', # h
            'w': 'West', # w
            's': 'South' # h
        }
        self.dir = 'e'
        

    def step(self, n: int) -> None:
        h, v = self.curr_loc
        width, height = self.width, self.height

        perimeter = 2 * (self.width + self.height)

        n = n % perimeter

        if h == 0 and v == 0:
            self.dir = 's'

        while n > 0:
            if self.dir =='e':
                if width >= h + n:
                    h  += n
                    break
                else:
                    n = n - (width - h)
                    h = width
                    self.dir = 'n'

            elif self.dir == 'n':
                if height >= v + n:
                    v += n
                    break
                else:
                    n = n - (height - v)
                    v = height
                    self.dir = 'w'

            elif self.dir == 'w':
                if 0 <= h - n:
                    h -= n
                    break
                else:
                    n = n - h
                    h = 0
                    self.dir = 's'

            elif self.dir == 's':
                if 0 <= v - n:
                    v -= n
                    break
                else:
                    n = n - v
                    v = 0
                    self.dir = 'e'

        self.curr_loc = [h,v]
        return
        

    def getPos(self) -> List[int]:
        return self.curr_loc
        

    def getDir(self) -> str:
        return self.allowed_dir[self.dir]
        


# Your Robot object will be instantiated and called as such:
# obj = Robot(width, height)
# obj.step(num)
# param_2 = obj.getPos()
# param_3 = obj.getDir()