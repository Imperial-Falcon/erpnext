# ERPNext Project Overview

ERPNext is a comprehensive, open-source Enterprise Resource Planning (ERP) solution built on the [Frappe Framework](https://github.com/frappe/frappe). It is designed to manage various business processes including accounting, inventory, manufacturing, CRM, and more.

## Architecture

ERPNext follows the Frappe Framework's modular architecture:

- **App Structure**: The `erpnext` directory is a Frappe "app".
- **Modules**: Business logic is divided into modules (e.g., `accounts`, `stock`, `buying`, `selling`, `manufacturing`).
- **DocTypes**: The core building blocks. Each DocType defines a database schema, controller logic, and frontend behavior.
  - Located in: `erpnext/<module>/doctype/<doctype_name>/`
  - `.json`: Schema definition and metadata.
  - `.py`: Python controller (server-side logic).
  - `.js`: JavaScript client-side script.
- **Hooks**: Integration with the Frappe system is defined in `erpnext/hooks.py`.
- **Frontend**: Uses Frappe's built-in Desk UI, with some custom components using Vue and `frappe-ui`.

## Tech Stack

- **Backend**: Python (>= 3.10)
- **Frontend**: JavaScript, Vue.js (for some parts), Frappe UI
- **Database**: MariaDB (default) or PostgreSQL
- **Caching/Task Queue**: Redis, Celery (via Frappe)
- **CLI**: `bench` (The Frappe CLI)

## Backend Development Workflow

### Building and Running

ERPNext must be run within a `frappe-bench` environment.

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
- **Run Migrations**: (Required after pulling changes or changing DocTypes)
  ```bash
  bench --site [your-site-name] migrate
  ```

### Testing

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

### Coding Standards

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

## Key Files

- `erpnext/hooks.py`: Main configuration for the app, including hooks, event handlers, and asset inclusions.
- `pyproject.toml`: Python dependencies and tool configurations.
- `package.json`: Frontend dependencies.
- `erpnext/accounts/doctype/sales_invoice/sales_invoice.py`: Example of a complex server-side controller.

# ERPNext B2B Mobile Apps

This is a Vue 3 and Ionic-based mobile application that serves as a B2B ordering portal for ERPNext. It is designed to be integrated directly into a Frappe environment.

**Apps Working Directory:** `frontend/apps`
Current B2B customer app working directory: `frontend/apps/b2b`
All file paths and code generation should assume this directory as the root unless specified otherwise.

## Project Overview

- **Purpose**: A mobile-first B2B ordering portal for ERPNext customers.
- **Tech Stack**:
  - **Frontend**: Vue 3, Vite, Ionic Vue, TailwindCSS.
  - **Framework Integration**: `frappe-ui` for data fetching, resources, and UI components.
  - **State Management**: Reactive objects and `frappe-ui` resources.
  - **PWA/Mobile**: Ionic Framework, Vite PWA plugin, Frappe Push Notifications.
- **Key Features**:
  - Product browsing and category filtering.
  - Shopping cart and checkout workflow.
  - Order history and reordering.
  - B2B-specific requests (e.g., medicine requests).
  - Real-time updates via Socket.io.
  - Push notifications.

## Architecture

- **`src/`**: Main source code.
  - **`components/`**: Reusable Vue components (using Ionic and Frappe UI).
  - **`views/`**: Page-level components (Home, Products, Cart, etc.).
  - **`data/`**: Data models and `frappe-ui` resource definitions (Session, User, Employee, Products, etc.).
  - **`router/`**: Ionic Vue Router configuration.
  - **`utils/`**: Helper functions, formatters, and Ionic configuration.
  - **`plugins/`**: Custom Vue plugins (e.g., translations).
- **`public/`**: Static assets and service workers.
- **`vite.config.js`**: Configured to proxy API requests to a Frappe backend and build assets into the `erpnext` app's public folder.

## Building and Running

### Prerequisites

- A running Frappe environment (`frappe-bench`).
- Node.js and Yarn/NPM.

### Development

1. Navigate to the app directory:

   ```bash
   cd apps/erpnext/frontend/apps/b2b
   ```
2. Install dependencies:

   ```bash
   yarn
   ```
3. Configure your Frappe site for development:
   In `sites/[your-site]/site_config.json`, add:

   ```json
   "ignore_csrf": 1
   ```
4. Start the development server:

   ```bash
   yarn dev
   ```

   The app will be available at `http://[your-site]:8080/b2b`.


## Tech Stack & Core Libraries

- **Framework:** Vue 3 (Composition API, `<script setup>`)
- **Mobile UI & Routing:** `@ionic/vue`, `@ionic/vue-router`, `vue-router`
- **Styling:** Tailwind CSS (`tailwindcss`, `autoprefixer`, `postcss`, `@tailwindcss/aspect-ratio`)
- **Backend/Services:** `frappe-ui` (for Frappe backend integration), `firebase`
- **PWA & Offline:** `vite-plugin-pwa`, `workbox-core`, `workbox-precaching`
- **Utilities:** `dayjs` (date manipulation)
- **Icons:** `lucide-vue-next`, `feather-icons`
- **Build Tool:** Vite (`vite`, `@vitejs/plugin-vue`)

## Coding Standards & Guidelines

### Vue & Architecture

- **Composition API:** Always use Vue 3 `<script setup>` syntax. Avoid the Options API.
- **State Management:** Use Vue's reactivity (`ref`, `reactive`, `computed`) or Frappe UI's built-in resource management.
- **Component Design:** Keep components modular. Separate business logic from UI where possible using composables (`useSomething.js`).

### UI & Styling (Ionic + Tailwind)

- **Mobile-First Layout:** Prioritize `@ionic/vue` components (e.g., `IonPage`, `IonHeader`, `IonContent`, `IonTabs`) for the core app skeleton, transitions, and native-feeling interactions.
- **Styling:** Use Tailwind CSS utility classes for styling, layout adjustments, and typography within the Ionic components. Avoid writing custom CSS unless absolutely necessary.
- **Icons:** Prefer `lucide-vue-next` for Vue components. If integrating with legacy components, use `feather-icons`.

### Production Build

To build the app for production and sync it with the Frappe app:

```bash
yarn build
```

This builds the assets into `erpnext/public/frontend/apps/b2b` and copies the entry point to `erpnext/www/b2b.html`.

## Development Conventions

- **Tab Indentation**: Follows the Frappe standard (Tabs for both JS and Python).
- **Component Styling**: Uses TailwindCSS for utility-first styling.
- **Data Fetching**: Use `frappe-ui`'s `createResource` or `call` for interacting with the backend.
- **Routing**: Use `@ionic/vue-router` for mobile-optimized navigation.
- **Auth**: Authentication is handled via Frappe session cookies. Navigation guards in `src/main.js` manage access control.
- **Mocking for Dev**: The app uses a special Frappe method `/api/method/erpnext.www.b2b.get_context_for_dev` to fetch boot data during development.

## Key Files

- `package.json`: Defines scripts and dependencies.
- `vite.config.js`: Manages proxying to the Frappe backend and build output paths.
- `src/main.js`: Entry point, initializes Ionic, Frappe UI, and Push Notifications.
- `src/router/index.js`: Defines all B2B portal routes.
- `src/data/session.js`: Manages user login, logout, and session state.
