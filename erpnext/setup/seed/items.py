import frappe
from erpnext.classes.seed_reader import SeedFileReader

# def seed_items(force=False):
# 	seed_item_groups(force=force)

def seed_warehouses(force=False):
    """
    Seed Warehouses from CSV

    CSV Columns:
    - warehouse_name
    - parent_warehouse
    - company
    - is_group
    """

    app_name = "erpnext"
    csv_filename = "warehouses.csv"
    doctype = "Warehouse"

    reader = SeedFileReader(app_name)
    rows = reader.read_csv(csv_filename)

    # Sort so parent warehouses are created before children
    rows = sorted(
        rows,
        key=lambda x: (x.get("parent_warehouse") or "") != ""
    )

    for row in rows:
        warehouse_name = row["warehouse_name"].strip()
        parent_warehouse = row.get("parent_warehouse")
        company = row["company"].strip()
        is_group = int(row.get("is_group", 0))

        if frappe.db.exists(doctype, warehouse_name):
            if not force:
                continue

            doc = frappe.get_doc(doctype, warehouse_name)
            doc.update({
                "parent_warehouse": parent_warehouse,
                "company": company,
                "is_group": is_group,
            })
            doc.save(ignore_permissions=True)

            frappe.logger().info(f"🔁 Updated Warehouse: {warehouse_name}")

        else:
            doc = frappe.get_doc({
                "doctype": doctype,
                "warehouse_name": warehouse_name,
                "parent_warehouse": parent_warehouse,
                "company": company,
                "is_group": is_group,
            })
            doc.insert(ignore_permissions=True)

            frappe.logger().info(f"🏬 Created Warehouse: {warehouse_name}")

def seed_item_groups(force=False):
    """
    Seed Item Groups from CSV
    CSV Columns:
    - item_group
    - parent_item_group
    - is_group
    """

    app_name = "erpnext"
    csv_filename = "item_groups.csv"
    doctype = "Item Group"

    reader = SeedFileReader(app_name)
    rows = reader.read_csv(csv_filename)

    # Sort so parents are created before children
    rows = sorted(rows, key=lambda x: x["parent_item_group"] != "All Item Groups")

    for row in rows:
        item_group = row["item_group"].strip()
        parent_item_group = row["parent_item_group"].strip()
        is_group = int(row.get("is_group", 1))

        if frappe.db.exists(doctype, item_group):
            if not force:
                continue

            doc = frappe.get_doc(doctype, item_group)
            doc.update({
                "parent_item_group": parent_item_group,
                "is_group": is_group,
            })
            doc.save(ignore_permissions=True)

            frappe.logger().info(f"🔁 Updated Item Group: {item_group}")

        else:
            doc = frappe.get_doc({
                "doctype": doctype,
                "item_group_name": item_group,
                "parent_item_group": parent_item_group,
                "is_group": is_group,
            })
            doc.insert(ignore_permissions=True)

            frappe.logger().info(f"📦 Created Item Group: {item_group}")
