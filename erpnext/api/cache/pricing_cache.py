import frappe
from ..repositories import pricing_rule_repository

CACHE_KEY = "item_pricing_rules"


def get_pricing_rules():

    cache = frappe.cache()

    rules = cache.get_value(CACHE_KEY)

    if not rules:
        rules = pricing_rule_repository.get_pricing_rules()
        cache.set_value(CACHE_KEY, rules, expires_in_sec=3600)

    return rules
