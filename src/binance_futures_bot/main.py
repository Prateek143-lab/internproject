# main.py

import logging
from binance_futures_bot.cli import main_cli
from binance_futures_bot.logging_config import setup_logging

def main():
    setup_logging()
    logging.info("Starting Binance Futures CLI Bot")
    main_cli()

if __name__ == "__main__":
    main()