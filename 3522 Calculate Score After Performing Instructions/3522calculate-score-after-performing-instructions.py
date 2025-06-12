class Solution:
    def calculateScore(self, instructions: List[str], values: List[int]) -> int:
        n, idx, val = len(values),0,0
        while 0<=idx<n and instructions[idx]:
            instr, instructions[idx]=instructions[idx], None
            if instr =='add':
                val+=values[idx]
                idx+=1
            else:
                idx+=values[idx]
        return val