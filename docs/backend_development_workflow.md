# Backend Development Workflow

ERPNext must be run within a `frappe-bench` environment to function correctly. The backend primarily uses Python over the Frappe Framework.

## Building and Running

- **Start Development Server**:
  ```bash
  bench start
  ```
- **Build Assets**:
  ```bash
  bench build --app erpnext
  ```
- **Watch Assets**:
  ```bash
  bench watch
  ```
- **Run Migrations**: (Required after pulling changes or altering DocType schemas)
  ```bash
  bench --site [your-site-name] migrate
  ```

## Testing

- **Run All Tests**:
  ```bash
  bench --site [your-site-name] run-tests --app erpnext
  ```
- **Run Specific Module Tests**:
  ```bash
  bench --site [your-site-name] run-tests --module erpnext.accounts
  ```
- **Run Specific DocType Tests**:
  ```bash
  bench --site [your-site-name] run-tests --doctype "Sales Invoice"
  ```

## Coding Standards

- **Indentation**: Use **Tabs** for both Python and JavaScript (Frappe standard).
- **Linting**: Uses `ruff` for Python.
  ```bash
  ruff check .
  ```
- **Formatting**:
  ```bash
  ruff format .
  ```
- **Naming**: Follow Frappe's naming conventions (CamelCase for DocTypes, snake_case for fields and functions).
