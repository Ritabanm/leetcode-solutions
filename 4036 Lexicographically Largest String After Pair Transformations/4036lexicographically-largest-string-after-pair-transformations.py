class Solution:
    def largestString(self, nums: list[int]) -> list[str]:
        def f(cnt,val):

            if val == "z":
                return cnt*val
            if cnt==1:
                return val
           
            if cnt%2==1:
                return f((cnt-1)//2,chr(ord(val) + 1))+val
            else:
                return f(cnt//2,chr(ord(val) + 1))

        ans=[]
        for i in range(len(nums)):
            ans.append(f(nums[i],"a"))
        return ans