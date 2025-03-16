class Solution:
    def mostFrequentPrime(self, mat: List[List[int]]) -> int:

        nums = []
        m,n, d = range(len(mat)),range(len(mat[0])), (-1,0,1)
        
        def isPrime(num):
            if num < 10 or num%2 == 0: return False
            for i in range(3, isqrt(num)+1, 2):
                if num %i == 0: return False
            return True
        
        for x, y, dx,dy in product(m,n, d,d):
                if dx == 0 == dy: continue
                X, Y, num = x+dx, y+dy, mat[x][y]

                while X in m and Y in n:
                    nums.append(num:= num*10 + mat[X][Y])
                    X+= dx
                    Y+= dy      
        
        return max(filter(isPrime, ctr:= Counter(nums)), 
                key = lambda x: (ctr[x], x), default = -1)