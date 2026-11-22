from __future__ import annotations

from dataclasses import dataclass


@dataclass(frozen=True, slots=True)
class Item:
    item_name: str
    quantity: int
    price: float

    def __post_init__(self) -> None:
        if self.quantity < 0 or self.price < 0:
            raise ValueError("quantity and price must be non-negative")

    @property
    def value(self) -> float:
        return self.quantity * self.price


items: list[Item] = [
    Item("Notebook", 50, 350.0),
    Item("Pen", 200, 100.0),
    Item("Stapler", 15, 1200.0),
    Item("Marker", 4, 450.0),
]


def low_stock(data: list[Item], threshold: int = 10) -> list[Item]:
    """New feature: items whose quantity is below ``threshold``."""
    return [i for i in data if i.quantity < threshold]
