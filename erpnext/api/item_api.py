import frappe

from .services import item_service


@frappe.whitelist(allow_guest=False)
def get_items(page=1, page_size=20, item_group=None, search=None):

    page = int(page)
    page_size = int(page_size)

    return item_service.get_items(
        page=page,
        page_size=page_size,
        item_group=item_group,
        search=search,
    )
