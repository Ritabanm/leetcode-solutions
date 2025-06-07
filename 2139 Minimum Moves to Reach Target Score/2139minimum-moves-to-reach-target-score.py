class Solution:
    def minMoves(self, target: int, maxD: int) -> int:
        if maxD == 0:
            return target-1
        
        count = 0
        while target>1:
            if maxD>0 and target%2 == 0:
                target = target/2
                maxD = maxD-1
                count += 1
            else:
                target = target-1
                count += 1
                
            if maxD == 0:
                count += target-1
                return int(count)
        
        return int(count)