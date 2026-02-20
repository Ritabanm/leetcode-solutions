class Solution:
    def countMonobit(self, n: int) -> int:
        count = 0
        for i in range(n+1):
            b = bin(i)[2:]
            if b.count('0')==len(b) or b.count('1')==len(b):
                count+=1
        return count