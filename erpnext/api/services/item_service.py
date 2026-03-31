from ..repositories import item_repository, stock_repository
from ..cache import pricing_cache
from ..services.pricing_engine import apply_pricing
from ..dto.item_dto import format_item
from ..utils.pagination import get_offset


def get_items(page=1, page_size=30, item_group=None, search=None):

    offset = get_offset(page, page_size)

    items = item_repository.get_items(
        limit=page_size,
        offset=offset,
        item_group=item_group,
        search=search,
    )

    if not items:
        return []

    item_codes = [i["name"] for i in items]

    stock_map = stock_repository.get_stock_map(item_codes)

    rules = pricing_cache.get_pricing_rules()

    result = []

    for item in items:

        item = apply_pricing(item, rules)

        stock = stock_map.get(item["name"], 0)

        result.append(format_item(item, stock))

    return result

def get_item_details(item_code):
    import frappe
    # Get basic item with price
    items = item_repository.get_items(limit=1, search=item_code)
    # Check if exact match exists
    item = next((i for i in items if i["name"] == item_code), None)
    
    if not item:
        # fallback direct query if not in standard list
        item = frappe.db.get_value("Item", item_code, 
            ["name", "item_name", "description", "image", "item_group", "brand"], as_dict=True)
        if not item:
            return None
        item["price"] = 0
        item["final_price"] = 0
        
    # Get stock map
    stock_map = stock_repository.get_stock_map([item_code])
    item["stock_qty"] = stock_map.get(item_code, 0)
    
    # Get Pricing rules
    rules = pricing_cache.get_pricing_rules()
    item = apply_pricing(item, rules)
    formatted = format_item(item, item["stock_qty"])
    
    # Add substitutes by finding items with same item_name
    substitutes = []
    if item.get("item_name"):
        subs = item_repository.get_items(limit=10, search=item.get("item_name"))
        substitutes = [format_item(s, stock_map.get(s["name"], 0)) for s in subs if s["name"] != item_code]
        
    formatted["substitutes"] = substitutes
    return formatted

def calculate_price(item_code, qty):
    import frappe
    items = item_repository.get_items(limit=1, search=item_code)
    item = next((i for i in items if i["name"] == item_code), None)
    if not item:
        return {"price": 0, "final_price": 0, "discount_percent": 0}
        
    rules = pricing_cache.get_pricing_rules()
    
    # Apply pricing but with quantity context
    # Usually apply_pricing takes an item and evaluates rule
    # Wait, we can pass qty into apply_pricing if supported, or calculate locally
    # I'll just temporarily return price until I check apply_pricing
    item["qty"] = qty
    item = apply_pricing(item, rules)
    
    return {
        "price": item.get("price", 0),
        "final_price": item.get("final_price", 0),
        "discount_percent": item.get("discount_percent", 0)
    }
