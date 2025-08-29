import argparse
import logging
from binance_futures_bot.client import BinanceClient
from binance_futures_bot.orders.market import MarketOrder
from binance_futures_bot.orders.limit import LimitOrder
from binance_futures_bot.validation.validators import validate_order

def setup_logging():
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s')

def parse_arguments():
    parser = argparse.ArgumentParser(description='Binance Futures CLI Trading Bot')
    parser.add_argument('--order_type', choices=['market', 'limit'], required=True, help='Type of order to place')
    parser.add_argument('--symbol', required=True, help='Trading pair symbol (e.g., BTCUSDT)')
    parser.add_argument('--quantity', type=float, required=True, help='Quantity to trade')
    parser.add_argument('--price', type=float, help='Price for limit order (required for limit orders)')
    
    return parser.parse_args()

def main():
    setup_logging()
    args = parse_arguments()

    if args.order_type == 'limit' and args.price is None:
        logging.error("Price must be specified for limit orders.")
        return

    if not validate_order(args.symbol, args.quantity, args.price):
        logging.error("Invalid order parameters.")
        return

    client = BinanceClient()

    if args.order_type == 'market':
        order = MarketOrder(symbol=args.symbol, quantity=args.quantity)
        response = client.place_order(order)
    else:
        order = LimitOrder(symbol=args.symbol, quantity=args.quantity, price=args.price)
        response = client.place_order(order)

    logging.info(f"Order response: {response}")

if __name__ == '__main__':
    main()