import json

from google.oauth2 import service_account
from google.cloud import firestore
from scrapy.conf import settings

credentials = service_account.Credentials.from_service_account_info(
    info=json.loads(settings["GCS_CREDENTIALS"])
)

db = firestore.Client(credentials=credentials, project=settings["GCS_PROJECT_ID"])


class FirestorePipeline:

    def __init__(self):
        self.ref = db.collection(settings["GCS_COLLECTION_NAME"])

    def process_item(self, item, _spider):
        self.ref.add(dict(item))
        return item
