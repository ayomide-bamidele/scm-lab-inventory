from __future__ import annotations

from inventory import Item, items, low_stock
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(data: list[Item]) -> float:
    return sum(i.value for i in data)


def format_report(data: list[Item]) -> str:
    width = max((len(i.item_name) for i in data), default=4)
    width = max(width, len("Item"))
    lines = [f"{'Item':<{width}} | {'Qty':>5} | {'Price':>10} | {'Value':>12}",
             f"{'-' * width}-+-{'-' * 5}-+-{'-' * 10}-+-{'-' * 12}"]
    for i in data:
        lines.append(f"{i.item_name:<{width}} | {i.quantity:>5} | {i.price:>10,.2f} | {i.value:>12,.2f}")
    lines.append(f"{'TOTAL':<{width}} | {'':>5} | {'':>10} | {total_stock_value(data):>12,.2f}")
    return "\n".join(lines)


def main() -> None:
    print("=== Inventory Report ===")
    print(format_report(items))
    high, low = highest_stock_item(items), lowest_stock_item(items)
    print(f"\nHighest stock: {high.item_name if high else 'n/a'}")
    print(f"Lowest stock : {low.item_name if low else 'n/a'}")
    print("Low stock (<10):", ", ".join(i.item_name for i in low_stock(items)) or "none")


if __name__ == "__main__":
    main()
