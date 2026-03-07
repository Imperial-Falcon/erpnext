import frappe

def get_active_pricing_rules():

    return frappe.db.sql("""
        SELECT
            name,
            item_code,
            brand,
            item_group,
            min_qty,
            discount_percentage,
            price_list_rate
        FROM `tabPricing Rule`
        WHERE
            selling = 1
            AND disabled = 0
    """, as_dict=True)
