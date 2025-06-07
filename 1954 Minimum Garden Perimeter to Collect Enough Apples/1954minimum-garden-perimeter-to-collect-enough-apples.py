class Solution:
    def minimumPerimeter(self, neededApples: int) -> int:
            i, summ, curr = 0, 0, 0
            while True:
                curr = 3*i+(2*i-1)*2*i - i*(i+1)
                summ += 4*curr
                if summ >= neededApples:
                    return i*4*2
                i+=1
                