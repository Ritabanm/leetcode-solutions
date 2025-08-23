class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        properties.sort(key = lambda x : (-x[0],x[1]))
        
        ans = 0
        curr_max = 0
        
        for attack,defend in properties:
            if defend < curr_max:
                ans+=1
            curr_max = max(curr_max, defend)
        return ans