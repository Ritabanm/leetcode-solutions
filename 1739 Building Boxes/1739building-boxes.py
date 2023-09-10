class Solution:
    def minimumBoxes(self, n):
        x = int((6*n)**(1/3))
        if x*(x+1)*(x+2) > 6*n: x -= 1 
        rem = n - x*(x+1)*(x+2)//6
        return x*(x+1)//2 + math.ceil((math.sqrt(1+8*rem)-1)/2)