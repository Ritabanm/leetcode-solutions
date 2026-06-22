class Solution:
    def countCompleteDayPairs(self, hours):

        ctr = Counter(map(lambda x: x %24, hours))

        count = sum(ctr[i] * ctr[24-i]
                                   for i in range(1, 12))
            
        return count + (ctr[12] * (ctr[12] - 1) + 
                                ctr[0] * (ctr[0] - 1))//2