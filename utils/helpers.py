def highest_stock_item(data):
    return max(data, key=lambda i: i["quantity"])


def lowest_stock_item(data):
    return min(data, key=lambda i: i["quantity"])
