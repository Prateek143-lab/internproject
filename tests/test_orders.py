import pytest
from binance_futures_bot.orders.market import MarketOrder
from binance_futures_bot.orders.limit import LimitOrder
from binance_futures_bot.models.order import Order

def test_market_order_creation():
    order = MarketOrder(symbol='BTCUSDT', quantity=0.01)
    assert order.symbol == 'BTCUSDT'
    assert order.quantity == 0.01
    assert order.order_type == 'MARKET'

def test_limit_order_creation():
    order = LimitOrder(symbol='BTCUSDT', quantity=0.01, price=50000)
    assert order.symbol == 'BTCUSDT'
    assert order.quantity == 0.01
    assert order.price == 50000
    assert order.order_type == 'LIMIT'

def test_order_model():
    order = Order(symbol='ETHUSDT', quantity=0.5, order_type='LIMIT', price=4000)
    assert order.symbol == 'ETHUSDT'
    assert order.quantity == 0.5
    assert order.order_type == 'LIMIT'
    assert order.price == 4000

def test_invalid_market_order():
    with pytest.raises(ValueError):
        MarketOrder(symbol='', quantity=0.01)

def test_invalid_limit_order():
    with pytest.raises(ValueError):
        LimitOrder(symbol='BTCUSDT', quantity=0.01, price=-1)