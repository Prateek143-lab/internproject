class OrderType:
    MARKET = "market"
    LIMIT = "limit"

class OrderStatus:
    PENDING = "pending"
    FILLED = "filled"
    CANCELED = "canceled"

class Order:
    def __init__(self, order_type: str, symbol: str, quantity: float, price: float = None):
        self.order_type = order_type
        self.symbol = symbol
        self.quantity = quantity
        self.price = price
        self.status = OrderStatus.PENDING

    def __repr__(self):
        return f"<Order(type={self.order_type}, symbol={self.symbol}, quantity={self.quantity}, price={self.price}, status={self.status})>"