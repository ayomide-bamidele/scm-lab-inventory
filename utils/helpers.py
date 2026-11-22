"""Helper functions for inventory analysis."""
from __future__ import annotations

from inventory import Item


def highest_stock_item(data: list[Item]) -> Item | None:
    """Return the item with the largest quantity, or None for an empty list."""
    return max(data, key=lambda i: i.quantity, default=None)


def lowest_stock_item(data: list[Item]) -> Item | None:
    """Return the item with the smallest quantity, or None for an empty list."""
    return min(data, key=lambda i: i.quantity, default=None)
