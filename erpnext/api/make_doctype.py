import frappe

def run():
    doctype_name = "Customer Viewed Item"
    if frappe.db.exists("DocType", doctype_name):
        print(f"DocType {doctype_name} already exists.")
    else:
        doc = frappe.get_doc({
            "doctype": "DocType",
            "name": doctype_name,
            "module": "Core",
            "custom": 1,
            "istable": 0,
            "naming_rule": "Expression",
            "autoname": "format:{user}-{item_code}-{viewed_on}",
            "fields": [
                {
                    "fieldname": "user",
                    "label": "User",
                    "fieldtype": "Link",
                    "options": "User",
                    "reqd": 1,
                    "in_list_view": 1
                },
                {
                    "fieldname": "item_code",
                    "label": "Item",
                    "fieldtype": "Link",
                    "options": "Item",
                    "reqd": 1,
                    "in_list_view": 1
                },
                {
                    "fieldname": "viewed_on",
                    "label": "Viewed On",
                    "fieldtype": "Datetime",
                    "default": "Now",
                    "reqd": 1,
                    "in_list_view": 1
                }
            ]
        })
        doc.insert(ignore_permissions=True)
        frappe.db.commit()
        print(f"Successfully created {doctype_name} DocType.")
