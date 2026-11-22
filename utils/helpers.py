from __future__ import annotations

from inventory import Item


def highest_stock_item(data: list[Item]) -> Item | None:
    return max(data, key=lambda i: i.quantity, default=None)


def lowest_stock_item(data: list[Item]) -> Item | None:
    return min(data, key=lambda i: i.quantity, default=None)
