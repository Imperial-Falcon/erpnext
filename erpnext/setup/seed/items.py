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

def seed_items(force=False):
    """
    Seed Items from CSV

    CSV Columns:
    - sn
    - disabled
    - is_sales_item
    - is_purchase_item
    - manufacturer_full_name
    - manufacturer_short_name
    - manufacturer_code
    - dosage_form
    - dosage_form_short_name
    - brand
    - item_group
    - generic_name
    - strength
    - stock_uom
    - mrp
    - sale_price
    - purchase_price
    """

    app_name = "erpnext"
    csv_filename = "items.csv"
    doctype = "Item"

    reader = SeedFileReader(app_name)
    rows = reader.read_csv(csv_filename)

    for row in rows:

        # --------------------------------------------------
        # CLEAN VALUES
        # --------------------------------------------------

        manufacturer_name = (row.get("manufacturer_full_name") or "").strip()
        manufacturer_short_name = (row.get("manufacturer_short_name") or "").strip()
        brand_name = (row.get("brand") or "").strip()
        item_group_name = (row.get("item_group") or "").strip()
        uom_name = (row.get("stock_uom") or "").strip()
        dosage_form_name = (row.get("dosage_form") or "").strip()
        dosage_form_short_name = (row.get("dosage_form_short_name") or "").strip()
        generic_name = (row.get("generic_name") or "").strip()
        strength = (row.get("strength") or "").strip()
        variant = (row.get("variant") or "").strip()
        disabled = int(row.get("disabled", 0))
        is_sales_item = int(row.get("is_sales_item", 1))
        is_purchase_item = int(row.get("is_purchase_item", 1))
        manufacturer_part_no = row.get("manufacturer_code")
        # sale_price = (row.get("sale_price") or "").strip()
        mrp = parse_price(row["mrp"])
        purchase_price = parse_price(row["purchase_price"])

        # --------------------------------------------------
        # GENERATE ITEM NAME + CODE
        # item_name = dosage_form_code + "." + brand + " " + variant
        # item_code = UPPER + kebab-case
        # --------------------------------------------------

        strength_formatted = strength.replace(" ", "").strip()
        variant_formatted = variant.replace(" ", "").strip()
        item_name = f"{dosage_form_short_name}. {brand_name} {strength_formatted} {variant_formatted}".strip()

        strength_formatted = strength_formatted.replace("+", " ").replace("/", " ").replace("%", " ").strip()
        variant_formatted = variant_formatted.replace("+", " ").replace("/", " ").replace("%", " ").strip()
        item_code = (
            f"{dosage_form_short_name} {brand_name} {strength_formatted} {variant_formatted}".strip()
            .upper()
            .replace(" ", "-")
        )

        # --------------------------------------------------
        # LINK OR CREATE MASTER DATA
        # --------------------------------------------------

        manufacturer = get_or_create_manufacturer("Manufacturer", manufacturer_short_name, manufacturer_name)
        brand = get_or_create_brand("Brand", manufacturer_short_name, brand_name)
        uom = get_or_create_uom("UOM", uom_name)
        item_group = item_group_name
        # Custom doctypes (adjust if different)
        dosage_form = get_or_create_dosage_form("Dosage Form", dosage_form_name, dosage_form_short_name)
        generic = get_or_create_generic("Generic Name", generic_name)

        # --------------------------------------------------
        # CREATE / UPDATE ITEM
        # --------------------------------------------------

        if frappe.db.exists(doctype, item_code):

            if not force:
                continue

            item = frappe.get_doc(doctype, item_code)

            item.update({
                "item_name": item_name,
                "disabled": disabled,
                "is_sales_item": is_sales_item,
                "is_purchase_item": is_purchase_item,
                "brand": brand,
                "item_group": item_group,
                "stock_uom": uom,
                "generic_name": generic,
                "dosage_form": dosage_form,
                "strength": strength,
            })

            item.save(ignore_permissions=True)

            frappe.logger().info(f"🔁 Updated Item: {item_code}")

        else:

            item = frappe.get_doc({
                "doctype": doctype,
                "item_code": item_code,
                "item_name": item_name,
                "disabled": disabled,
                "is_sales_item": is_sales_item,
                "is_purchase_item": is_purchase_item,
                "brand": brand,
                "item_group": item_group,
                "stock_uom": uom,
                "generic_name": generic,
                "dosage_form": dosage_form,
                "strength": strength,
            })

            item.insert(ignore_permissions=True)

            frappe.logger().info(f"📦 Created Item: {item_code}")

        # capture generated name
        item_name_doc = item.name
        # --------------------------------------------------
		# CREATE ITEM PRICES
		# --------------------------------------------------

        create_or_update_item_price(
			item_code=item_name_doc,
			uom=uom,
			price_list="Standard Selling",
			price=mrp
		)

        create_or_update_item_price(
			item_code=item_name_doc,
			uom=uom,
			price_list="Standard Buying",
			price=purchase_price
		)

# ----------------------------------------------------------
# HELPER FUNCTION
# ----------------------------------------------------------

def get_or_create_manufacturer(doctype, short_name, full_name=None):
    """
    Generic safe master-data creator.
    Returns name or None.
    """

    if not short_name:
        return None

    short_name = short_name.strip()

    docname = frappe.db.exists(
        doctype,
        {"short_name": short_name}
    )

    if docname:
        return docname

    doc = frappe.get_doc({
        "doctype": doctype,
        "short_name": short_name,
        "full_name": full_name or short_name,
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(f"✨ Created {doctype}: {full_name}")

    return doc.name

def get_or_create_brand(doctype, manufacturer, brand):
    """
    Generic safe master-data creator.
    Returns name or None.
    """

    if not brand:
        return None

    docname = frappe.db.exists(
        doctype,
        {"brand": brand}
    )

    if docname:
        return docname

    doc = frappe.get_doc({
        "doctype": doctype,
        "manufacturer": manufacturer,
        "brand": brand
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(f"✨ Created {doctype}: {brand}")

    return doc.name

def get_or_create_uom(doctype, uom_name):
    """
    Generic safe master-data creator.
    Returns name or None.
    """
    uom_name = uom_name.strip()

    if not uom_name:
        return None

    docname = frappe.db.exists(
        doctype,
        {"uom_name": uom_name}
    )

    if docname:
        return docname

    doc = frappe.get_doc({
        "doctype": doctype,
        "uom_name": uom_name
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(f"✨ Created {doctype}: {uom_name}")

    return doc.name

def get_or_create_dosage_form(doctype, full_name, short_name):
    """
    Safe master-data creator for Dosage Form.
    Ensures code_name is always generated.
    """

    if not full_name:
        return None

    full_name = full_name.strip()
    short_name = (short_name or "").strip()

    # --------------------------------------------------
    # CHECK EXISTING
    # --------------------------------------------------

    docname = frappe.db.exists(
        doctype,
        {"full_name": full_name}
    )

    if docname:
        return docname

    # --------------------------------------------------
    # CREATE
    # --------------------------------------------------

    doc = frappe.get_doc({
        "doctype": doctype,
        "full_name": full_name,
        "short_name": short_name or full_name
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(f"✨ Created {doctype}: {full_name}")

    return doc.name

def get_or_create_generic(doctype, display_name):
    """
    Generic safe master-data creator.
    Returns name or None.
    """

    if not display_name:
        return None

    docname = frappe.db.exists(
        doctype,
        {"display_name": display_name}
    )

    if docname:
        return docname

    doc = frappe.get_doc({
        "doctype": doctype,
        "display_name": display_name
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(f"✨ Created {doctype}: {display_name}")

    return doc.name

def create_or_update_item_price(item_code, uom, price_list, price):
    """
    Create or update Item Price safely
    """

    if not price:
        return

    doctype = "Item Price"

    docname = frappe.db.exists(
        doctype,
        {
            "item_code": item_code,
            "price_list": price_list
        }
    )

    if docname:

        doc = frappe.get_doc(doctype, docname)

        if doc.price_list_rate != price:
            doc.price_list_rate = price
            doc.save(ignore_permissions=True)

            frappe.logger().info(
                f"💲 Updated {price_list} price for {item_code}: {price}"
            )

        return

    doc = frappe.get_doc({
        "doctype": doctype,
        "item_code": item_code,
        "uom": uom,
        "price_list": price_list,
        "price_list_rate": price,
        "currency": "BDT",
        "selling": 1 if price_list == "Standard Selling" else 0,
        "buying": 1 if price_list == "Standard Buying" else 0
    })

    doc.insert(ignore_permissions=True)

    frappe.logger().info(
        f"💲 Created {price_list} price for {item_code}: {price}"
    )

def parse_price(value):
    if not value:
        return 0
    return float(str(value).replace(",", "").strip())
