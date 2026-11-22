from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(data):
    total = 0
    for item in data:
        total += item["quantity"] * item["price"]  # value = quantity x unit price
    return total


def main():
    print("Total stock value:", total_stock_value(items))
    for label, func in (("Highest", highest_stock_item), ("Lowest", lowest_stock_item)):
        found = func(items)
        print(f"{label} stock:", found["item_name"] if found else "n/a")


if __name__ == "__main__":
    main()
