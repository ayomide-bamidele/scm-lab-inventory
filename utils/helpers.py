def highest_stock_item(data):
    if not data:
        return None
    return max(data, key=lambda i: i["quantity"])


def lowest_stock_item(data):
    if not data:
        return None
    return min(data, key=lambda i: i["quantity"])
