class Solution:
    def relocateMarbles(self, nums: List[int], moveFrom: List[int], moveTo: List[int]) -> List[int]:
        value=dict()
        for n in nums:
            if n in value:
                value[n]+=1
            else:
                value[n]=1
        for i in range(len(moveFrom)):
            if moveFrom[i]!=moveTo[i]:
                if moveTo[i] in value:
                    value[moveTo[i]]+=value[moveFrom[i]]
                else:
                    value[moveTo[i]]=value[moveFrom[i]]
                value[moveFrom[i]]=0
            
        ans=list()
            
        for i in value.keys():
            if value[i]!=0:
                ans.append(i)
                
        return sorted(ans)