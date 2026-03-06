def item_card(row):

    return {
        "id": row["name"],
        "name": row["item_name"],
        "brand": row["brand"],
        "image": row["image"],
        "price": row["price"],
        "mrp": row["mrp"],
        "discount": row["discount_percent"]
    }
