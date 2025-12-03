from numpy import array, round
from numpy.fft import fft, ifft as invFft

class Solution:
    def multiply(self, poly1: List[int], poly2: List[int]) -> List[int]:

        n1, n2 = len(poly1), len(poly2)
        n = n1 + n2 - 1

        size = 1 << (n-1).bit_length()              #
        arr1 = array(poly1 + [0] * (size - n1))     # <-- 1)
        arr2 = array(poly2 + [0] * (size - n2))     #
        
        ans  = invFft(fft(arr1) * fft(arr2))        # <-- 2)
                                           
        return round(ans).astype(int).tolist()[:n]  # <-- 3)