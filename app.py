from inventory import items
from utils.helpers import highest_stock_item, lowest_stock_item


def total_stock_value(data):
    total = 0
    for item in data:
        total += item["quantity"] + item["price"]  # calculates stock value
    return total


print("Total stock value:", total_stock_value(items))
print("Highest stock:", highest_stock_item(items)["item_name"])
print("Lowest stock:", lowest_stock_item(items)["item_name"])
