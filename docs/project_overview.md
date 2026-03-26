# ERPNext Project Overview

ERPNext is a comprehensive, open-source Enterprise Resource Planning (ERP) solution built on the [Frappe Framework](https://github.com/frappe/frappe). It manages various business processes including accounting, inventory, manufacturing, CRM, and more.

## High-Level Architecture
- **App Structure**: The `erpnext` directory is a built-in Frappe "app".
- **Modules**: Business logic is divided into major sections (e.g., `accounts`, `stock`, `buying`, `selling`, `manufacturing`).
- **DocTypes**: The core functional building blocks of Frappe.
  - Defined in `erpnext/<module>/doctype/<doctype_name>/`
  - Comprised of a JSON definition (schema/metadata), a Python controller (backend), and a JavaScript script (frontend).
- **Core Integrations**: Integration hooks, routing, webhooks, portal views, and scheduling are connected in `erpnext/hooks.py`.
- **Database**: Uses MariaDB or PostgreSQL. Caching and scheduled tasks are run via Redis and Celery.
- **Frontend App**: This specific fork includes a custom Vue.js `b2b` mobile application located in `frontend/apps/b2b`.
