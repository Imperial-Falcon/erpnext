import frappe

from .services import item_service


@frappe.whitelist(allow_guest=False)
def get_items(page=1, page_size=30, item_group=None, search=None):

    page = int(page)
    page_size = int(page_size)

    return item_service.get_items(
        page=page,
        page_size=page_size,
        item_group=item_group,
        search=search,
    )

@frappe.whitelist(allow_guest=False)
def get_item_details(item_code):
    return item_service.get_item_details(item_code)

@frappe.whitelist(allow_guest=False)
def calculate_price(item_code, qty=1):
    return item_service.calculate_price(item_code, float(qty))

@frappe.whitelist(allow_guest=False)
def log_item_view(item_code):
    if not frappe.db.exists("Item", item_code):
        return
    
    doc = frappe.new_doc("Customer Viewed Item")
    doc.user = frappe.session.user
    doc.item_code = item_code
    doc.insert(ignore_permissions=True)
    frappe.db.commit()
    return "Logged"

@frappe.whitelist(allow_guest=False)
def get_recently_viewed_items(limit=10):
    user = frappe.session.user
    views = frappe.get_all(
        "Customer Viewed Item", 
        filters={"user": user}, 
        fields=["item_code"], 
        order_by="viewed_on desc", 
        limit_page_length=int(limit)
    )
    
    if not views:
        return []
        
    # Deduplicate while preserving order
    seen = set()
    unique_items = []
    for v in views:
        if v.item_code not in seen:
            seen.add(v.item_code)
            unique_items.append(v.item_code)
            
    # fetch details using item_service
    results = []
    for code in unique_items:
        details = item_service.get_item_details(code)
        if details:
            results.append(details)
            
    return results
