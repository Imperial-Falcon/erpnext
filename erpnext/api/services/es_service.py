import frappe
import json

try:
    from elasticsearch import Elasticsearch
except ImportError:
    Elasticsearch = None

class ESService:
    def __init__(self):
        self.index_name = "erpnext_items"
        # We assume ES is available at elasticsearch:9200 or via frappe site config
        self.es_url = frappe.conf.get("elasticsearch_url", "http://elasticsearch:9200")
        if Elasticsearch:
            self.client = Elasticsearch([self.es_url])
        else:
            self.client = None

    def index_item(self, item_doc):
        if not self.client:
            return
        
        doc = {
            "name": item_doc.name,
            "item_name": item_doc.item_name,
            "description": item_doc.description,
            "item_group": item_doc.item_group,
            "brand": item_doc.brand,
        }
        try:
            self.client.index(index=self.index_name, id=item_doc.name, document=doc)
        except Exception as e:
            frappe.log_error(f"Failed to index item {item_doc.name} to ES: {str(e)!r}", "Elasticsearch Sync")

    def delete_item(self, item_name):
        if not self.client:
            return
        try:
            self.client.delete(index=self.index_name, id=item_name, ignore=[404])
        except Exception as e:
            frappe.log_error(f"Failed to delete item {item_name} from ES: {str(e)!r}", "Elasticsearch Sync")

    def search_items(self, search_term, limit=30, offset=0):
        if not self.client:
            return []
            
        try:
            res = self.client.search(
                index=self.index_name,
                body={
                    "query": {
                        "match": {
                            "item_name": {
                                "query": search_term,
                                "fuzziness": "AUTO"
                            }
                        }
                    },
                    "from": offset,
                    "size": limit
                }
            )
            hits = res.get("hits", {}).get("hits", [])
            return [hit["_id"] for hit in hits]
        except Exception as e:
            frappe.log_error(f"ES Search failed: {str(e)!r}", "Elasticsearch Search")
            return []

es_service = ESService()

def sync_item_on_update(doc, method):
    es_service.index_item(doc)

def sync_item_on_trash(doc, method):
    es_service.delete_item(doc.name)
