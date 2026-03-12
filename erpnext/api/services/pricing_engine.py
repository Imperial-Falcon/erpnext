def apply_pricing(item, rules, qty=1):

    base_price = item.get("price") or 0
    final_price = base_price
    discount = 0

    for rule in rules:

        item_code = rule.get("item_code")

        if item_code and item_code != item["name"]:
            continue

        min_qty = rule.get("min_qty") or 0
        if min_qty and qty < min_qty:
            continue

        discount_percentage = rule.get("discount_percentage")
        rate = rule.get("rate")

        # Discount rule
        if discount_percentage:
            new_price = base_price * (1 - discount_percentage / 100)

            if new_price < final_price:
                final_price = new_price
                discount = discount_percentage

        # Fixed rate rule
        elif rate:
            if rate < final_price:
                final_price = rate
                discount = round((1 - final_price / base_price) * 100)

    item["final_price"] = round(final_price, 2) if final_price else 0
    item["discount_percent"] = discount

    return item
