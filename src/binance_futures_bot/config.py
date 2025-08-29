# Configuration settings for the Binance Futures trading bot

import os

class Config:
    API_KEY = os.getenv("BINANCE_API_KEY")
    API_SECRET = os.getenv("BINANCE_API_SECRET")
    BASE_URL = "https://fapi.binance.com"
    TIMEOUT = 30  # seconds

    # Trading settings
    DEFAULT_SYMBOL = "BTCUSDT"
    DEFAULT_QUANTITY = 0.01
    LEVERAGE = 20

    # Logging settings
    LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
    LOG_FILE = os.getenv("LOG_FILE", "trading_bot.log")

    # Order settings
    MAX_OPEN_ORDERS = 5
    ORDER_EXPIRATION = 60  # seconds

    @staticmethod
    def validate():
        if not Config.API_KEY or not Config.API_SECRET:
            raise ValueError("API_KEY and API_SECRET must be set in the environment variables.")