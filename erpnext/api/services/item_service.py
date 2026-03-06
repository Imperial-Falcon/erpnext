from erpnext.api.repositories.item_repository import fetch_home_items
from erpnext.api.cache.item_cache import get_cache, set_cache
from erpnext.api.dto.item_dto import item_card


def get_home_items(limit=20, offset=0):

    cache_key = f"home_items:{limit}:{offset}"

    cached = get_cache(cache_key)
    if cached:
        return cached

    rows = fetch_home_items(limit, offset)

    items = [item_card(row) for row in rows]

    set_cache(cache_key, items)

    return items
