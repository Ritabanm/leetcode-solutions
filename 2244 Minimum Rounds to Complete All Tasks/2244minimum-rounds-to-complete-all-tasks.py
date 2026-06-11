class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        d, count = Counter(tasks), 0
        if 1 in d.values():
            return -1
        
        for i in d.values():
            count+= (i+2)//3
        return count