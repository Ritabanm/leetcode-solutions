class Solution:
    def countEven(self, num: int) -> int:
        count = 0
        for i in range(2, num+1):
            if sum(list(map(int, str(i).strip())))%2==0:
                count+=1
        return count