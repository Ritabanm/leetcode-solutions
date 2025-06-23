class Solution:
    def preimageSizeFZF(self, k: int) -> int:  

        count = lambda x: 0 if x == 0 else x//5 + count(x//5)
        
        atLeast_K = lambda x: bisect_right(range(5*x + 5), x, key = count)

        return atLeast_K(k) - atLeast_K(k-1)