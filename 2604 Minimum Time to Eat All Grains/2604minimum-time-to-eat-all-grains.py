class Solution:
    def minimumTime(self, hens: List[int], grains: List[int]) -> int:
        
        grains.sort()
        hens.sort()
        n = len(grains)
        
        def ispossible(time):
            j = 0
            for i in hens:
                dist = max(i-grains[j], 0)
                if dist > time:
                    continue
                if i > grains[j]:
                    j += 1
                while j < n and grains[j] < i:
                    j += 1
                
                # go left first
                temp = j
                while temp < n and grains[temp]-i+2*dist <= time:
                    temp += 1
                left_ans = temp
                
                #go right first
                temp = j
                while temp < n and 2*(grains[temp]-i)+dist <= time:
                    temp += 1
                right_ans = temp

                j = max(left_ans, right_ans)
                if j >= n:
                    return 1
            return 0


        return bisect.bisect(range(10000000000), 0, key=ispossible)


                