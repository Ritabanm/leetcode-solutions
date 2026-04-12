class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        found = [False,False,False]
        foundCount = 0
        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]: 
                #Useless Triplet
                continue
            if a==target[0] and found[0]==False:
                found[0] = True
                foundCount += 1
            if b==target[1]  and found[1]==False:
                found[1] = True
                foundCount += 1
            if c==target[2] and found[2]==False:
                found[2] = True
                foundCount += 1
            
            if foundCount==3:
                break

        return True if foundCount==3 else False

