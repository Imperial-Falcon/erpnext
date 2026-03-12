import frappe


def get_stock_map(item_codes):

    if not item_codes:
        return {}

    data = frappe.db.sql(
        """
        SELECT
            item_code,
            SUM(actual_qty) AS qty
        FROM `tabBin`
        WHERE item_code IN %(items)s
        GROUP BY item_code
        """,
        {"items": tuple(item_codes)},
        as_dict=True,
    )

    return {d.item_code: d.qty for d in data}
