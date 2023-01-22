class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sum=0
        for i  in nums:
            if(i>9):
                s=0
                temp=i
                while(temp!=0):
                    r=temp%10
                    s+=r
                    temp//=10
                sum+=s
            else:
                sum+=i
        sum2=0
        for i in nums:
            sum2+=i
        return abs(sum-sum2)
            

        