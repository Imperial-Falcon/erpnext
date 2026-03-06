import frappe


def fetch_home_items(limit, offset):

    query = """
        SELECT
            i.name,
            i.item_name,
            i.image,
            i.brand,

            mrp.price_list_rate AS mrp,
            sell.price_list_rate AS price,

            ROUND(
                ((mrp.price_list_rate - sell.price_list_rate) /
                mrp.price_list_rate) * 100
            ) AS discount_percent

        FROM `tabItem` i

        INNER JOIN `tabItem Price` mrp
            ON mrp.item_code = i.name
            AND mrp.price_list = 'Maximum Retail Price'

        INNER JOIN `tabItem Price` sell
            ON sell.item_code = i.name
            AND sell.price_list = 'Standard Selling'

        WHERE
            i.disabled = 0
            AND i.is_sales_item = 1
            AND i.has_variants = 0

        ORDER BY i.creation DESC

        LIMIT %(limit)s
        OFFSET %(offset)s
    """

    return frappe.db.sql(
        query,
        {"limit": limit, "offset": offset},
        as_dict=True
    )
