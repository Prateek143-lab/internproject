class MarketOrder:
    def __init__(self, client, symbol, quantity):
        self.client = client
        self.symbol = symbol
        self.quantity = quantity

    def validate(self):
        if not self.symbol or not isinstance(self.symbol, str):
            raise ValueError("Invalid symbol provided.")
        if self.quantity <= 0:
            raise ValueError("Quantity must be greater than zero.")

    def place_order(self):
        self.validate()
        try:
            response = self.client.futures_create_order(
                symbol=self.symbol,
                side='BUY',
                type='MARKET',
                quantity=self.quantity
            )
            return response
        except Exception as e:
            raise RuntimeError(f"Failed to place market order: {str(e)}")