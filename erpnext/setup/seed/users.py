import frappe
from frappe.utils import today, add_years
from erpnext.classes.seed_reader import SeedFileReader


def seed_users(force=False):
    app_name = "erpnext"
    csv_filename = "users.csv"
    user_doctype = "User"
    employee_doctype = "Employee"

    reader = SeedFileReader(app_name)
    users = reader.read_csv(csv_filename)

    default_company = frappe.defaults.get_global_default("Company")

    for row in users:
        email = row["email"].strip()

        # -----------------------------
        # USER CREATE / UPDATE
        # -----------------------------
        if frappe.db.exists(user_doctype, email):
            if not force:
                user = frappe.get_doc(user_doctype, email)
            else:
                user = frappe.get_doc(user_doctype, email)
                user.update({
                    "first_name": row["first_name"],
                    "enabled": int(row.get("enabled", 1)),
                    "roles": [
                        {"role": r.strip()}
                        for r in row["roles"].split("|")
                    ],
                })
                user.save(ignore_permissions=True)

                if row.get("password"):
                    user.new_password = row["password"]
                    user.save(ignore_permissions=True)
        else:
            user = frappe.get_doc({
                "doctype": user_doctype,
                "email": email,
                "first_name": row["first_name"],
                "enabled": int(row.get("enabled", 1)),
                "user_type": "System User",
                "send_welcome_email": 0,
                "roles": [
                    {"role": r.strip()}
                    for r in row["roles"].split("|")
                ],
            })
            user.insert(ignore_permissions=True)

            if row.get("password"):
                user.new_password = row["password"]
                user.save(ignore_permissions=True)

        if default_company:
            frappe.defaults.set_user_default(
                "Company",
                default_company,
                email
            )

        frappe.logger().info(f"👤 Seeded user: {email}")

        # -----------------------------
        # EMPLOYEE CREATE / UPDATE
        # -----------------------------
        employee_name = row["first_name"]

        existing_employee = frappe.db.get_value(
            employee_doctype,
            {"user_id": email},
            "name"
        )

        employee_data = {
            "first_name": employee_name,
            "gender": "Male",
            "salutation": "Mr",
            "user_id": email,
            "company": default_company,
            "date_of_joining": today(),
            "date_of_birth": add_years(today(), -25),
            "employment_type": "Full-time",
            "create_user_permission": True,
            "status": "Active"
        }

        if existing_employee:
            if force:
                employee = frappe.get_doc(employee_doctype, existing_employee)
                employee.update(employee_data)
                employee.save(ignore_permissions=True)
                frappe.logger().info(
                    f"🧑‍💼 Updated employee: {employee.first_name}"
                )
        else:
            employee = frappe.get_doc({
                "doctype": employee_doctype,
                **employee_data
            })
            employee.insert(ignore_permissions=True)

            frappe.logger().info(
                f"🧑‍💼 Created employee: {employee.first_name}"
            )
