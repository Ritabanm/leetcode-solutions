class Solution:
    def averageValue(self, nums: List[int]) -> int:
        tot, cnt = 0,0
        for num in nums:
            if num%6 ==0:
                tot+=num
                cnt+=1
        return tot//cnt if cnt else 0