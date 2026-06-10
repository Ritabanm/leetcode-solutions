class Solution:
    def maxTastiness(self, price, tastiness, maxAmount, maxCoupons):
        n = len(price)


        @lru_cache(None)
        def function(i,amount,coupon):
            if i >= n:
                return 0 

            max_val = function(i+1,amount,coupon)

            if coupon and amount-price[i]//2 >= 0:
                max_val = max(max_val,tastiness[i]+function(i+1,amount-price[i]//2,coupon-1))

            if amount-price[i] >= 0:
                max_val = max(max_val,tastiness[i]+function(i+1,amount-price[i],coupon))

            return max_val
        
        return function(0,maxAmount,maxCoupons)