import csv
import frappe
from pathlib import Path


class SeedFileReader:
    def __init__(self, app_name: str, seed_dir: str = "data/seed"):
        """
        :param app_name: Frappe app name (e.g. 'erpnext')
        :param seed_dir: Relative seed directory inside app
        """
        self.app_name = app_name
        self.seed_dir = seed_dir

    def _get_seed_path(self, filename: str) -> Path:
        app_path = frappe.get_app_path(self.app_name)
        path = Path(app_path) / self.seed_dir / filename

        if not path.exists():
            frappe.throw(f"Seed file not found: {path}")

        return path

    def read_csv(self, filename: str) -> list[dict]:
        """
        Reads a CSV file and returns list of rows as dictionaries
        """
        path = self._get_seed_path(filename)

        with open(path, newline="", encoding="utf-8") as f:
            return list(csv.DictReader(f))
