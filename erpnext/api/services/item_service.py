from ..repositories import item_repository, stock_repository
from ..cache import pricing_cache
from ..services.pricing_engine import apply_pricing
from ..dto.item_dto import format_item
from ..utils.pagination import get_offset


def get_items(page=1, page_size=20, item_group=None, search=None):

    offset = get_offset(page, page_size)

    items = item_repository.get_items(
        limit=page_size,
        offset=offset,
        item_group=item_group,
        search=search,
    )

    if not items:
        return []

    item_codes = [i["name"] for i in items]

    stock_map = stock_repository.get_stock_map(item_codes)

    rules = pricing_cache.get_pricing_rules()

    result = []

    for item in items:

        item = apply_pricing(item, rules)

        stock = stock_map.get(item["name"], 0)

        result.append(format_item(item, stock))

    return result
