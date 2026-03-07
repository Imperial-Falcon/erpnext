import click
import frappe

from erpnext.setup.seed.users import seed_users
from erpnext.setup.seed.items import seed_warehouses
from erpnext.setup.seed.items import seed_item_groups
from erpnext.setup.seed.manufacturers import seed_manufacturers
from erpnext.setup.seed.items import seed_items

@click.command("seed:dev")
@click.option("--site", required=False)
@click.option("--doctype", required=False, default="all", help="Specific doctype to run")
@click.option("--force", is_flag=True, default=False, help="Force re-seeding existing data")
@click.pass_context
def seed_dev(ctx, site, doctype, force):
    """Seed development-only data"""
    if not site:
        root = ctx.find_root()
        site = getattr(root.obj, "site", None)

    # 🔧 Initialize frappe manually
    frappe.init(site=site)
    frappe.connect()
    doctype = doctype.lower()

    try:
        # 🛑 DEV-ONLY SAFETY
        if not frappe.conf.get("developer_mode"):
            frappe.throw("❌ seed-dev allowed only in developer_mode")

        click.echo(f"🚀 Seeding DEV data for site: {site}")

        # -----------------------------
        # REAL SEED LOGIC
        # -----------------------------
        if doctype == "all" or doctype == "user":
            seed_users(force=force)
            click.echo("✅ Users seed completed successfully")
        if doctype == "all" or doctype == "warehouse":
            seed_warehouses(force=force)
            click.echo("✅ Warehouses seed completed successfully")
        if doctype == "all" or doctype == "item_group":
            seed_item_groups(force=force)
            click.echo("✅ Item groups seed completed successfully")
        if doctype == "all" or doctype == "manufacturer":
            seed_manufacturers(force=force)
            click.echo("✅ Manufacturers seed completed successfully")
        if doctype == "all" or doctype == "item":
            seed_items(force=force)
            click.echo("✅ Items seed completed successfully")

        frappe.db.commit()
        click.echo("✅ All seed completed successfully")

    finally:
        frappe.destroy()
