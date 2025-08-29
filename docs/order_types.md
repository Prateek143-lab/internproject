# Order Types Supported by the Trading Bot

This document outlines the different order types that the Binance USDT-M Futures trading bot supports. Understanding these order types is crucial for effectively using the bot and managing your trading strategy.

## 1. Market Orders

Market orders are executed immediately at the current market price. They are useful when you want to enter or exit a position quickly without worrying about the price. 

### Characteristics:
- **Execution Speed**: Fast, as they are filled at the best available price.
- **Price Certainty**: No guarantee on the execution price; it may vary based on market conditions.
- **Use Case**: Ideal for traders who prioritize speed over price.

### Example:
To place a market order, you would specify the symbol and quantity, and the bot will execute the order at the current market price.

## 2. Limit Orders

Limit orders allow you to specify the price at which you want to buy or sell an asset. The order will only be executed if the market reaches your specified price.

### Characteristics:
- **Execution Speed**: May take longer to fill, depending on market conditions.
- **Price Certainty**: Guarantees the price at which the order will be executed, but not the execution itself.
- **Use Case**: Suitable for traders who want to control the price at which they enter or exit a position.

### Example:
To place a limit order, you would specify the symbol, quantity, and the desired price. The bot will wait until the market price reaches your specified limit before executing the order.

## Conclusion

Both market and limit orders have their advantages and disadvantages. Choosing the right order type depends on your trading strategy and market conditions. The Binance USDT-M Futures trading bot supports both order types, allowing you to tailor your trading approach to your needs.