import click
import frappe

from erpnext.setup.seed.users import seed_users
from erpnext.setup.seed.items import seed_warehouses
from erpnext.setup.seed.items import seed_item_groups
from erpnext.setup.seed.manufacturers import seed_manufacturers
# from erpnext.setup.seed.items import seed_items

@click.command("seed:dev")
@click.option("--site", required=False)
@click.option("--seeder", required=False, default="all", help="Specific seeder to run")
@click.option("--force", is_flag=True, default=False, help="Force re-seeding existing data")
@click.pass_context
def seed_dev(ctx, site, seeder, force):
    """Seed development-only data"""
    if not site:
        root = ctx.find_root()
        site = getattr(root.obj, "site", None)

    # 🔧 Initialize frappe manually
    frappe.init(site=site)
    frappe.connect()
    seeder = seeder.lower()

    try:
        # 🛑 DEV-ONLY SAFETY
        if not frappe.conf.get("developer_mode"):
            frappe.throw("❌ seed-dev allowed only in developer_mode")

        click.echo(f"🚀 Seeding DEV data for site: {site}")

        # -----------------------------
        # REAL SEED LOGIC
        # -----------------------------
        if seeder == "all" or seeder == "users":
            seed_users(force=force)
            click.echo("✅ Users seed completed successfully")
        if seeder == "all" or seeder == "warehouses":
            seed_warehouses(force=force)
            click.echo("✅ Warehouses seed completed successfully")
        if seeder == "all" or seeder == "item_groups":
            seed_item_groups(force=force)
            click.echo("✅ Item groups seed completed successfully")
        if seeder == "all" or seeder == "manufacturers":
            seed_manufacturers(force=force)
            click.echo("✅ Manufacturers seed completed successfully")
        if seeder == "all" or seeder == "items":
            # seed_items(force=force)
            pass

        frappe.db.commit()
        click.echo("✅ All seed completed successfully")

    finally:
        frappe.destroy()
