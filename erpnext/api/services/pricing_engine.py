def apply_pricing_rules(item, rules, qty=1):

    best_price = item.base_price
    best_discount = 0

    for rule in rules:

        if rule.item_code and rule.item_code != item.name:
            continue

        if rule.min_qty and qty < rule.min_qty:
            continue

        if rule.discount_percentage:

            price = item.base_price * (1 - rule.discount_percentage / 100)

            if price < best_price:
                best_price = price
                best_discount = rule.discount_percentage

        elif rule.price_list_rate:

            if rule.price_list_rate < best_price:
                best_price = rule.price_list_rate
                best_discount = round(
                    (1 - best_price / item.mrp) * 100
                )

    item["final_price"] = round(best_price, 2)
    item["discount_percent"] = best_discount

    return item
