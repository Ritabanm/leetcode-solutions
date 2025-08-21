class Cashier:
    from collections import defaultdict
    def __init__(self, n: int, discount: int, products: List[int], prices: List[int]):
        self.n = n
        self.x = discount
        self.mp = defaultdict(int)
        for i in range(len(products)):
            self.mp[products[i]] = prices[i]
        self.ctr = 0

    def getBill(self, product: List[int], amount: List[int]) -> float:
        self.ctr += 1
        bill = 0
        for i in range(len(product)):
            bill += self.mp[product[i]] * amount[i]
        if (self.ctr % self.n == 0):
            disc = (self.x/100) * bill
            bill -= disc
        return bill