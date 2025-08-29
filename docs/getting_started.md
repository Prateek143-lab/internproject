# Getting Started with Binance Futures CLI Bot

Welcome to the Binance Futures CLI Bot! This guide will help you set up and run the bot on your local machine.

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.7 or higher
- pip (Python package installer)
- Git (optional, for cloning the repository)

## Installation

1. **Clone the repository** (if applicable):

   ```bash
   git clone https://github.com/yourusername/binance-futures-cli-bot.git
   cd binance-futures-cli-bot
   ```

2. **Create a virtual environment** (recommended):

   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use `venv\Scripts\activate`
   ```

3. **Install the required packages**:

   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. **Obtain your Binance API keys**:
   - Sign in to your Binance account.
   - Navigate to the API Management section and create a new API key.
   - Make sure to enable futures trading for the API key.

2. **Set up your configuration**:
   - Copy the `.env.example` file to `.env` and fill in your API keys and other necessary configurations.

## Running the Bot

To start the bot, you can use the provided shell script:

```bash
bash scripts/run_bot.sh
```

Alternatively, you can run the bot directly using Python:

```bash
python src/binance_futures_bot/main.py
```

## Usage

Once the bot is running, you can interact with it through the command-line interface. Use the help command to see available options:

```bash
python src/binance_futures_bot/cli.py --help
```

## Logging

The bot includes robust logging capabilities. Logs will be saved to the specified log file in the configuration. Check the logs for any errors or important information regarding the bot's operation.

## Support

If you encounter any issues or have questions, feel free to open an issue in the repository or reach out to the community for support.

Happy trading!