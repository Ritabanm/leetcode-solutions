class Solution:
    def alternateDigitSum(self, n: int) -> int:
        res = [int(num) for num in str(n)]
        se = 0
        sv = 0
        for i in range(0, len(res), 2):
            se+=res[i]
        for j in range(1, len(res), 2):
            sv+=(-res[j])
        
        return se+sv