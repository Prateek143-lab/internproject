import pytest

@pytest.fixture(scope="module")
def setup_bot():
    # Setup code for the trading bot
    pass

@pytest.fixture
def mock_order():
    # Mock order data for testing
    return {
        "symbol": "BTCUSDT",
        "quantity": 1,
        "price": 50000
    }