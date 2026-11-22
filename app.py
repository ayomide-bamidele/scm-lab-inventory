from __future__ import annotations

from inventory import Item, items, low_stock
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(data: list[Item]) -> float:
    return sum(i.value for i in data)


def main() -> None:
    print("Total stock value:", total_stock_value(items))
    for label, func in (("Highest", highest_stock_item), ("Lowest", lowest_stock_item)):
        found = func(items)
        print(f"{label} stock:", found.item_name if found else "n/a")
    print("Low stock:", [i.item_name for i in low_stock(items)])


if __name__ == "__main__":
    main()
