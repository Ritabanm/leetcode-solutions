"""class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        cnt,res = 0, k
        for num in nums:
            if  num > res:
                cnt += (c:= (num-res + k-1) //k)
                res += c * k
            res -= num
        return  (cnt * (cnt+1) //2) %int(1e9+7)
            
        """

class Solution:
    def minimumCost(self, nums, k):
        cnt, res = 0, k
        for num in nums:
            if num>res:
                cnt+= (c:=(num-res+k-1)//k)
                res+=c*k
            res-=num
        return (cnt*(cnt+1)//2)%int(1e9+7)