import pytest

from app import total_stock_value
from inventory import Item, low_stock
from utils.helpers import highest_stock_item, lowest_stock_item

DATA = [Item("A", 2, 10.0), Item("B", 5, 4.0), Item("C", 1, 100.0)]


def test_total_value_is_quantity_times_price():
    assert total_stock_value(DATA) == 2 * 10 + 5 * 4 + 1 * 100


def test_extremes():
    assert highest_stock_item(DATA).item_name == "B"
    assert lowest_stock_item(DATA).item_name == "C"


def test_empty_inventory():
    assert total_stock_value([]) == 0
    assert highest_stock_item([]) is None
    assert lowest_stock_item([]) is None


def test_low_stock_and_validation():
    assert [i.item_name for i in low_stock(DATA, threshold=3)] == ["A", "C"]
    with pytest.raises(ValueError):
        Item("bad", -1, 1.0)
