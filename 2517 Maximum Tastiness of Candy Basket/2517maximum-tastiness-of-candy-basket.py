class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        
        price.sort()

        def check(x):
            last, count, i = price[0], 1, 1

            for p in price[1:]:
                if p - last >= x:
                    last = p
                    count += 1
                if count >= k:
                    return True
            return False

        lo, hi = 0, price[- 1]
        
        while lo <= hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid - 1
        
        return hi