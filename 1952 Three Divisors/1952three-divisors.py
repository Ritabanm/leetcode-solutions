class Solution:
    def isThree(self, n: int) -> bool:
        # Check if n is a perfect square
        root = int(n ** 0.5)
        if root * root != n:
            return False
        
        # Check if the square root of n is a prime number
        for i in range(2, root):
            if root % i == 0:
                return False
        return root > 1