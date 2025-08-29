# Configuration Options for Binance Futures CLI Bot

This document outlines the configuration options available for the Binance Futures CLI Bot. Proper configuration is essential for the bot to function correctly and securely.

## Configuration File

The bot uses a configuration file to store essential settings. You can create a `config.py` file in the `src/binance_futures_bot` directory to define your configuration options.

### Required Configuration Options

1. **API Key**: Your Binance API key is required for authentication.
   ```python
   API_KEY = 'your_api_key_here'
   ```

2. **API Secret**: Your Binance API secret is required for authentication.
   ```python
   API_SECRET = 'your_api_secret_here'
   ```

3. **Base URL**: The base URL for the Binance Futures API.
   ```python
   BASE_URL = 'https://fapi.binance.com'
   ```

4. **Symbol**: The trading pair you wish to trade (e.g., 'BTCUSDT').
   ```python
   TRADING_SYMBOL = 'BTCUSDT'
   ```

5. **Leverage**: The leverage to be used for trading.
   ```python
   LEVERAGE = 20
   ```

### Optional Configuration Options

1. **Log Level**: The level of logging (e.g., DEBUG, INFO, WARNING, ERROR).
   ```python
   LOG_LEVEL = 'INFO'
   ```

2. **Order Timeout**: The timeout duration for order placement in seconds.
   ```python
   ORDER_TIMEOUT = 30
   ```

3. **Max Open Orders**: The maximum number of open orders allowed.
   ```python
   MAX_OPEN_ORDERS = 5
   ```

### Example Configuration

Here is an example of how your `config.py` might look:

```python
API_KEY = 'your_api_key_here'
API_SECRET = 'your_api_secret_here'
BASE_URL = 'https://fapi.binance.com'
TRADING_SYMBOL = 'BTCUSDT'
LEVERAGE = 20
LOG_LEVEL = 'INFO'
ORDER_TIMEOUT = 30
MAX_OPEN_ORDERS = 5
```

### Security Considerations

- **Keep your API keys secure**: Do not share your API keys or hard-code them in public repositories.
- **Use environment variables**: Consider using environment variables to store sensitive information securely.

### Conclusion

Proper configuration is crucial for the successful operation of the Binance Futures CLI Bot. Ensure that all required options are set correctly before running the bot.