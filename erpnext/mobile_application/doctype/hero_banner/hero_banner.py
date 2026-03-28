# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class HeroBanner(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		app_name: DF.Literal["B2B", "B2C"]
		background_gradient_from: DF.Color
		background_gradient_to: DF.Color
		banner_image: DF.AttachImage | None
		banner_title: DF.Data
		cta_bg_color: DF.Color | None
		cta_text: DF.Data | None
		cta_text_color: DF.Color | None
		end_date: DF.Datetime | None
		is_published: DF.Check
		sort_order: DF.Int
		start_date: DF.Datetime
		tag_bg_color: DF.Color | None
		tag_text: DF.Data | None
		tag_text_color: DF.Color | None
		target_route: DF.Data | None
		title_html: DF.SmallText | None
		title_text_color: DF.Color | None
	# end: auto-generated types

	pass
