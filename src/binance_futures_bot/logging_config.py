import logging

def setup_logging(log_file='trading_bot.log'):
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file),
            logging.StreamHandler()
        ]
    )

    logger = logging.getLogger('binance_futures_bot')
    logger.info('Logging is set up.')
    return logger