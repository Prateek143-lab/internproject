# Binance USDT-M Futures CLI Trading Bot

This project is a command-line interface (CLI) trading bot for Binance USDT-M Futures. It supports multiple order types, including market and limit orders, and is designed to be robust, with extensive logging and input validation.

## Features

- **Multiple Order Types**: Supports market and limit orders.
- **Robust Logging**: Configurable logging to track bot activity and errors.
- **Input Validation**: Ensures that all inputs are validated before placing orders.
- **Modular Design**: Organized into packages for easy maintenance and scalability.

## Getting Started

To get started with the Binance Futures CLI Bot, follow these steps:

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/binance-futures-cli-bot.git
   cd binance-futures-cli-bot
   ```

2. **Install Dependencies**:
   Make sure you have Python 3.7 or higher installed. Then, install the required packages:
   ```bash
   pip install -r requirements.txt
   ```

3. **Configure API Keys**:
   Create a `.env` file in the root directory and add your Binance API keys. You can refer to `docs/api_keys.md` for guidance on obtaining your API keys.

4. **Run the Bot**:
   You can run the bot using the provided shell script:
   ```bash
   ./scripts/run_bot.sh
   ```

## Documentation

- **[Getting Started](docs/getting_started.md)**: Detailed instructions on setting up and running the bot.
- **[Configuration](docs/configuration.md)**: Information on configuration options available for the bot.
- **[Order Types](docs/order_types.md)**: Explanation of the different order types supported by the bot.
- **[API Keys](docs/api_keys.md)**: Guidance on how to obtain and configure API keys for Binance.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any enhancements or bug fixes.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.