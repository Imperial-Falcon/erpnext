import frappe
from erpnext.classes.seed_reader import SeedFileReader

def seed_manufacturers(force=False):
    """
    Seed Manufacturers from CSV
    CSV Columns:
    - short_name
    - full_name
    - country
    """

    app_name = "erpnext"
    csv_filename = "manufacturers.csv"
    doctype = "Manufacturer"

    reader = SeedFileReader(app_name)
    rows = reader.read_csv(csv_filename)

    for row in rows:
        short_name = row["short_name"].strip()
        full_name = row["full_name"].strip()
        country = row["country"].strip()

        if frappe.db.exists(doctype, short_name):
            if not force:
                continue

            doc = frappe.get_doc(doctype, short_name)
            doc.update({
                "full_name": full_name,
                "country": country,
            })
            doc.save(ignore_permissions=True)

            frappe.logger().info(f"🔁 Updated Manufacturer: {short_name}")

        else:
            doc = frappe.get_doc({
                "doctype": doctype,
                "short_name": short_name,
                "full_name": full_name,
                "country": country
            })
            doc.insert(ignore_permissions=True)

            frappe.logger().info(f"🏭 Created Manufacturer: {short_name}")
