# Pharmoxy Project Overview (Doctoverse)

Pharmoxy is a comprehensive B2B E-commerce, ERP, and Webapp project, developed as a core product of Doctoverse. It is designed to manage full purchase, sales, distribution, accounting, and other critical business systems. Pharmoxy is a tailored fork of [ERPNext](https://github.com/frappe/erpnext), built upon the modular [Frappe Framework](https://github.com/frappe/frappe).

## Development Environment (Docker & WSL)

This project is configured as a **Frappe Docker (devcontainer)** setup running on a **Windows WSL** system.

### Accessing the Environment

All backend operations (`bench` commands, Python execution, etc.) and frontend tasks should be executed from within the Docker container.

To access the interactive bash shell of the development container, run:

```bash
docker exec -it devcontainer-frappe-1 bash
```

## Architecture

Pharmoxy follows the Frappe Framework's modular architecture:

- **App Structure**: The `erpnext` directory acts as our primary Frappe "app".
- **Modules**: Business logic is divided into modules (e.g., `accounts`, `stock`, `buying`, `selling`, `manufacturing`).
- **DocTypes**: The core building blocks for the schema and logic:
  - Located in: `erpnext/<module>/doctype/<doctype_name>/`
  - `.json`: Schema definition and metadata.
  - `.py`: Python controller (server-side logic).
  - `.js`: JavaScript client-side script.
- **Hooks**: App integration is centrally defined in `erpnext/hooks.py`.
- **Frontend**: Utilizes Frappe's Desk UI alongside our highly customized Vue-based B2B apps using `frappe-ui`.

## Tech Stack

- **Backend**: Python (>= 3.10)
- **Frontend**: JavaScript, Vue 3, Frappe UI, Ionic, TailwindCSS
- **Database**: MariaDB (default)
- **Caching/Task Queue**: Redis, Celery
- **CLI**: `bench` (The Frappe CLI)

## Backend Development Workflow

### Building and Running (Inside Devcontainer)

Ensure you are inside the `devcontainer-frappe-1` shell.

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
- **Run Migrations**: (Required after pulling changes or altering DocTypes)
  ```bash
  bench --site [your-site-name] migrate
  ```

### Testing

- **Run All Tests**:
  ```bash
  bench run-tests --app erpnext
  ```

### Coding Standards

- **Indentation**: Use **Tabs** for both Python and JavaScript (Frappe standard).
- **Linting**: Uses `ruff` for Python (`ruff check .`).
- **Formatting**: `ruff format .`
- **Naming**: Follow Frappe conventions (CamelCase for DocTypes, snake_case for fields/functions).

---

# Pharmoxy B2B Mobile App (Doctoverse)

This is a Vue 3 and Ionic-based mobile application that serves as the comprehensive B2B ecommerce ordering portal for Pharmoxy.

**Apps Working Directory:** `frontend/apps`
**Current B2B App Directory:** `frontend/apps/b2b`

_Note: All frontend file paths and module resolutions generally assume this directory as the root context._

## B2B App Overview

- **Purpose**: A mobile-first, high-performance B2B ordering portal.
- **Tech Stack**: Vue 3, Vite, Ionic Vue, TailwindCSS, `frappe-ui`.
- **Key Features**:
  - Medicine/Product browsing and categorization.
  - Cart, unified checkout, and multi-step workflows.
  - Detailed Order History and Reordering.
  - B2B-specific operational flows (medicine requests, bulk ordering).
  - High-end aesthetics encompassing Neon-accented Glassmorphic styling.

## B2B Architecture

- **`src/`**: Main source code.
  - **`components/`**: Reusable UI, leveraging Ionic and custom Tailwind styling.
  - **`views/`**: Page-level components.
  - **`data/`**: Data models and `frappe-ui` resource definitions (Session, Cart, Products).
  - **`router/`**: Ionic Vue Router handling navigations and guards.

## Building and Running the Frontend

### Prerequisites

Execute these from within the dev container (`docker exec -it devcontainer-frappe-1 bash`).

### Development

1. Navigate to the app directory:
   ```bash
   cd apps/erpnext/frontend/apps/b2b
   ```
2. Install dependencies:
   ```bash
   yarn install
   ```
3. Start the Vite development server:
   ```bash
   yarn dev
   ```
   _The app uses proxy setups in `vite.config.js` to route traffic to the Frappe backend. Dev environment fetches boot data via `/api/method/erpnext.www.b2b.get_context_for_dev`._

### Compilation / Build

To compile the standalone app into the Frappe public assets serving folder:

```bash
yarn build
```

## Frontend Standards & Aesthetics

- **Vue 3 `<script setup>`**: Exclusive use of Composition API.
- **Styling**: TailwindCSS driven designs over custom CSS blocks.
- **Vibe & Aesthetic**: Strictly "Neon-accented Glassmorphism" for a premium, mobile-first experience. Dynamic animations and rich gradients are prioritized.
- **State Management**: Using `frappe-ui` resources for seamless synchronization with the ERPNext base.

---
