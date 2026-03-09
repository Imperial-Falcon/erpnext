import frappe

CACHE_KEY = "homepage_items"


def get():

    return frappe.cache().get_value(CACHE_KEY)


def set(data):

    frappe.cache().set_value(CACHE_KEY, data, expires_in_sec=300)
