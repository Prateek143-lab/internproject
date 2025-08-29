class Order:
    def __init__(self, symbol: str, quantity: float, price: float = None):
        self.symbol = symbol
        self.quantity = quantity
        self.price = price

    def validate(self):
        if not isinstance(self.symbol, str) or not self.symbol:
            raise ValueError("Symbol must be a non-empty string.")
        if not isinstance(self.quantity, (int, float)) or self.quantity <= 0:
            raise ValueError("Quantity must be a positive number.")
        if self.price is not None and (not isinstance(self.price, (int, float)) or self.price <= 0):
            raise ValueError("Price must be a positive number if provided.")

    def to_dict(self):
        order_dict = {
            "symbol": self.symbol,
            "quantity": self.quantity,
        }
        if self.price is not None:
            order_dict["price"] = self.price
        return order_dict