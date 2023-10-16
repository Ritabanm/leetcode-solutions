class OrderManagementSystem:
    def __init__(self):
        self.orders = {} # orderId -> [type, price, i]
        self.orders_at_price = defaultdict(list) # (type, price) -> [orderId]

    def addOrder(self, orderId: int, orderType: str, price: int) -> None:
        self.orders_at_price[(orderType, price)].append(orderId)
        n = len(self.orders_at_price[(orderType, price)])
        self.orders[orderId] = [orderType, price, n - 1]

    def modifyOrder(self, orderId: int, newPrice: int) -> None:
        orderType, _, _ = self.orders[orderId] 
        self.cancelOrder(orderId)
        self.addOrder(orderId, orderType, newPrice)
        
    def cancelOrder(self, orderId: int) -> None:
        orderType, price, i = self.orders[orderId]
        orderIds = self.orders_at_price[(orderType, price)]
        last_val = orderIds[-1]
        last_type, last_price, n = self.orders[last_val]
        orderIds[i], orderIds[n] = orderIds[n], orderIds[i]
        orderIds.pop()
        self.orders[last_val][2] = i
        del self.orders[orderId]

    def getOrdersAtPrice(self, orderType: str, price: int) -> List[int]:
        return self.orders_at_price[(orderType, price)]
# Your OrderManagementSystem object will be instantiated and called as such:
# obj = OrderManagementSystem()
# obj.addOrder(orderId,orderType,price)
# obj.modifyOrder(orderId,newPrice)
# obj.cancelOrder(orderId)
# param_4 = obj.getOrdersAtPrice(orderType,price)