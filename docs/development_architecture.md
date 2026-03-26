# Development Architecture & Tech Stack

This repository splits work into two main sections:

## 1. Backend (ERPNext & Frappe)
- **Language**: Python (>= 3.10)
- **Framework**: Frappe Framework
- **Key Concepts**:
  - **DocTypes**: Manage database tables, Python controllers, and UI forms.
  - **Modules**: Grouped domains of business logic like `erpnext.accounts` and `erpnext.stock`.
  - **Hooks (`hooks.py`)**: Register scheduled jobs, custom APIs, DocType event overrides, and port endpoints.
- **Development Workflow**:
  - Operated heavily through the `bench` CLI.
  - Commands: `bench start` (server backend) and `bench --site [site-name] migrate` (database changes).
- **Formatting**: `ruff` for linting and code formatting in Python. Indentation strictly uses **Tabs** (Frappe standard) in both Python and JS.

## 2. Frontend Progressive Web App (B2B Portal)
Located inside `frontend/apps/b2b`, this is a high-performance Vue 3 app tailored for a mobile B2B experience.

- **Stack**: Vue 3 (`<script setup>`, Composition API), `@ionic/vue`, `@ionic/vue-router`, TailwindCSS.
- **Data Flow**: Connects to the ERPNext backend utilizing `frappe-ui` resources for login/session caching and HTTP request handling without typical raw Axios endpoints.
- **PWA Features**: Uses Firebase pushes and `vite-plugin-pwa` for offline caching (`workbox-core`).
- **Development Workflow**:
  - Run locally utilizing Vite via `yarn dev` pointing to `port 8080`.
  - Vite automatically proxies API calls `^/(api|app|login)` to the Frappe backend running on port `8000`.
  - Built into `../../../erpnext/public/frontend/apps/b2b` and deployed automatically into ERPNext's public `/www` application route using `yarn build`.
