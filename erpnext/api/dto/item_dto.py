def format_item(item, stock):

    return {
        "name": item["name"],
        "item_name": item["item_name"],
        "image": item["image"],
        "brand": item["brand"],
        "manufacturer": item.get("manufacturer") or "",
        "item_group": item["item_group"],
        "price": item["price"],
        "final_price": item["final_price"],
        "discount_percent": item["discount_percent"],
        "stock_qty": stock,
    }
