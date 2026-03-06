import frappe
from erpnext.api.services.item_service import get_home_items


@frappe.whitelist(allow_guest=False)
def home_items(limit=20, offset=0):

	return get_home_items(
		limit=int(limit),
		offset=int(offset)
	)
