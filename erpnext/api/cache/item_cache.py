import frappe

TTL = 60


def get_cache(key):
    return frappe.cache().get_value(key)


def set_cache(key, value):
    frappe.cache().set_value(key, value, expires_in_sec=TTL)
