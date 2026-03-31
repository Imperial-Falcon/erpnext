import frappe

from ..constants.price_lists import STANDARD_SELLING


def get_items(limit=30, offset=0, item_group=None, search=None):
    from ..services.es_service import es_service

    conditions = ["i.disabled = 0", "i.is_sales_item = 1"]

    if item_group:
        conditions.append("i.item_group = %(item_group)s")

    if search:
        es_item_codes = es_service.search_items(search, limit=limit, offset=offset)
        if not es_item_codes:
            return []
        
        safe_codes = [frappe.db.escape(c) for c in es_item_codes]
        format_strings = ','.join(safe_codes)
        conditions.append(f"i.name IN ({format_strings})")
        order_by = f"ORDER BY FIELD(i.name, {format_strings})"
        limit_clause = ""
    else:
        order_by = "ORDER BY i.creation DESC"
        limit_clause = "LIMIT %(limit)s OFFSET %(offset)s"

    where = " AND ".join(conditions)

    return frappe.db.sql(
        f"""
        SELECT
            i.name,
            i.item_name,
            i.image,
            i.item_group,
            i.brand,
            b.manufacturer,
            COALESCE(p.price_list_rate,0) AS price,
            COALESCE(pr.discount_percentage,0) AS discount_percent,
            ROUND(
                COALESCE(p.price_list_rate,0)
                -
                (COALESCE(p.price_list_rate,0) * COALESCE(pr.discount_percentage,0) / 100)
            ,2) AS final_price,
            COALESCE(SUM(bin.actual_qty),0) AS stock_qty

        FROM `tabItem` i
        LEFT JOIN `tabBrand` b ON b.name = i.brand
        INNER JOIN `tabItem Price` p ON p.item_code = i.name AND p.price_list = %(price_list)s
        LEFT JOIN `tabPricing Rule Item Code` pri ON pri.item_code = i.name
        LEFT JOIN `tabPricing Rule` pr ON pr.name = pri.parent AND pr.selling = 1 AND pr.disable = 0
        LEFT JOIN `tabBin` bin ON bin.item_code = i.name

        WHERE {where}
        GROUP BY i.name
        {order_by}
        {limit_clause}
        """,
        {
            "price_list": STANDARD_SELLING,
            "limit": limit,
            "offset": offset,
            "item_group": item_group,
        },
        as_dict=True,
    )
