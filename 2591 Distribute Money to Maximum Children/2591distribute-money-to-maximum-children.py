class Solution:
    def distMoney(self, money: int, children: int) -> int:
        
        if money<children:
            return -1
        
        n = 8*children-money

        if n<=0:
            return children - (n<0)
        
        ans, rem = divmod(money-children,7)

        return ans-((ans, rem)==(children-1,3))