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
        thread_doc = self.ref.document(item.id)

        self.__create_or_update_thread(thread_doc, dict(item))
        return item

    def __create_or_update_thread(self, document, params):
        thread_snapshot = document.get()
        thread_exists = thread_snapshot.exists

        if thread_exists:
            has_changes = self.__check_for_changes(params, thread_snapshot.to_dict())
            if has_changes:
                document.set(params, {"merge": True})
        else:
            document.set(params)

    @staticmethod
    def __check_for_changes(old_values, new_values):
        if old_values["replies_count"] != new_values["replies_count"]:
            return True

        return False
