class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        b=''.join(map(str,b))
        b=int(b)
        return (pow(a,b,1337))