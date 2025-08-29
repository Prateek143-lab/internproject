class BaseOrder:
    def __init__(self, symbol: str, quantity: float):
        self.symbol = symbol
        self.quantity = quantity

    def validate(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def execute(self):
        raise NotImplementedError("Subclasses should implement this method.")

    def __repr__(self):
        return f"<BaseOrder(symbol={self.symbol}, quantity={self.quantity})>"