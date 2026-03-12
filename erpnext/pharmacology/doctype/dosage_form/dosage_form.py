# Copyright (c) 2026, Frappe Technologies Pvt. Ltd. and contributors
# For license information, please see license.txt

# import frappe
from frappe.model.document import Document


class DosageForm(Document):
	# begin: auto-generated types
	# This code is auto-generated. Do not modify anything in this block.

	from typing import TYPE_CHECKING

	if TYPE_CHECKING:
		from frappe.types import DF

		full_name: DF.Data
		is_group: DF.Check
		lft: DF.Int
		old_parent: DF.Link | None
		parent_dosage_form: DF.Link | None
		rgt: DF.Int
		short_name: DF.Data
	# end: auto-generated types

	pass
