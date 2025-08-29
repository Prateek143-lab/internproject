from binance.client import Client
import logging

class BinanceFuturesClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret)
        self.logger = self.setup_logging()

    def setup_logging(self):
        logger = logging.getLogger("BinanceFuturesClient")
        logger.setLevel(logging.INFO)
        handler = logging.StreamHandler()
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        return logger

    def get_account_info(self):
        try:
            account_info = self.client.futures_account()
            self.logger.info("Fetched account info successfully.")
            return account_info
        except Exception as e:
            self.logger.error(f"Error fetching account info: {e}")
            raise

    def place_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        try:
            if order_type == 'MARKET':
                order = self.client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
            elif order_type == 'LIMIT':
                order = self.client.futures_create_order(symbol=symbol, side=side, type=order_type, quantity=quantity, price=price)
            else:
                self.logger.error("Invalid order type specified.")
                raise ValueError("Invalid order type specified.")
            self.logger.info(f"Order placed: {order}")
            return order
        except Exception as e:
            self.logger.error(f"Error placing order: {e}")
            raise

    def get_open_orders(self, symbol: str):
        try:
            open_orders = self.client.futures_get_open_orders(symbol=symbol)
            self.logger.info("Fetched open orders successfully.")
            return open_orders
        except Exception as e:
            self.logger.error(f"Error fetching open orders: {e}")
            raise