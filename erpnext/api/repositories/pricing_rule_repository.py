import frappe


def get_pricing_rules():

    return frappe.db.sql(
        """
        SELECT
            pr.name AS rule_name,
            pri.item_code,
            pr.min_qty,
            pr.discount_percentage,
            pr.rate

        FROM `tabPricing Rule` pr

        LEFT JOIN `tabPricing Rule Item Code` pri
            ON pri.parent = pr.name

        WHERE
            pr.selling = 1
            AND pr.docstatus < 2
        """,
        as_dict=True,
    )
