class Solution:
    def shoppingOffers(self, price: List[int], special: List[List[int]], needs: List[int]) -> int:
        
        n = len(price)

        @lru_cache(None)
        def solve(needs_left):
            needs_arr = list(map(int , needs_left.split()))
        
            if sum(needs_arr)==0:
                return 0
            lowestPrice = sum([needs_arr[idx]*price[idx] for idx in range(n)])
            for offer in special:
                offer_price = offer[n]
                flag = True
                needs_after_offer = []
                for idx in range(n):
                    if needs_arr[idx] < offer[idx]:
                        flag = False
                        break
                    else:
                        needs_after_offer.append(str(needs_arr[idx]-offer[idx]))
                        
                if flag:
                    lowestPrice = min(lowestPrice , offer_price+solve(" ".join(needs_after_offer)))
            return lowestPrice
        needs2 = [str(i) for i in needs]
        return solve(" ".join(needs2))
                