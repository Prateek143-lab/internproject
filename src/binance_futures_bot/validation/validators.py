def validate_symbol(symbol):
    if not isinstance(symbol, str) or len(symbol) == 0:
        raise ValueError("Symbol must be a non-empty string.")
    # Additional symbol validation logic can be added here

def validate_quantity(quantity):
    if not isinstance(quantity, (int, float)) or quantity <= 0:
        raise ValueError("Quantity must be a positive number.")

def validate_price(price):
    if not isinstance(price, (int, float)) or price <= 0:
        raise ValueError("Price must be a positive number.")

def validate_order(order):
    validate_symbol(order['symbol'])
    validate_quantity(order['quantity'])
    if 'price' in order:
        validate_price(order['price'])