import pytest
from binance_futures_bot.validation.validators import validate_symbol, validate_quantity, validate_price

def test_validate_symbol_valid():
    assert validate_symbol("BTCUSDT") is True

def test_validate_symbol_invalid():
    assert validate_symbol("INVALID") is False

def test_validate_quantity_valid():
    assert validate_quantity(0.01) is True
    assert validate_quantity(1) is True

def test_validate_quantity_invalid():
    assert validate_quantity(0) is False
    assert validate_quantity(-1) is False

def test_validate_price_valid():
    assert validate_price(50000) is True
    assert validate_price(0.01) is True

def test_validate_price_invalid():
    assert validate_price(0) is False
    assert validate_price(-1) is False