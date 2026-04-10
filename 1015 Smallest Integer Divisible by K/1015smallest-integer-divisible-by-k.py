class Solution:
    def smallestRepunitDivByK(self,k):
        rem = 0
        for len_n in range(1, k+1):
            rem = (rem*10+1)%k
            if rem ==0:
                return len_n
        return -1


"""class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder =0
        for length_n in range(1,k+1):
            remainder = (remainder*10+1)%k
            if remainder == 0:
                return length_n
        return -1"""